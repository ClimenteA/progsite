import datetime
from pytz import timezone
from apps.crm.models.availability import Availability, Entry
from apps.crm.models.collections import AppointmentCol, SiteDataCol
from common.logger import log
from common.password import encrypt
from common.responses import CustomResponse
from apps.crm.models.appointment import SetAppointmentModel
from apps.crm.models.sitedata import (
    SiteDataModel,
    TIMEUNIT,
    BizzServiceModel,
    TimeFrameModel,
)


def get_free_intervals(
    day_entries: list[TimeFrameModel] | None,
    interval: datetime.timedelta,
    avail_day,
    date_now,
):
    if day_entries is None:
        return

    avail_day_date = datetime.datetime.fromisoformat(avail_day.date).date()
    available = date_now.date() <= avail_day_date

    free_intervals = {}
    for entry in day_entries:
        start_time = datetime.datetime.strptime(entry.start, "%H:%M")
        stop_time = datetime.datetime.strptime(entry.stop, "%H:%M")
        current_time = start_time
        while current_time < stop_time:
            next_time = current_time + interval
            if next_time > stop_time and current_time - next_time == interval:
                next_time = stop_time
            if next_time > stop_time:
                current_time = stop_time
                continue

            intervalstr = (
                f'{current_time.strftime("%H:%M")} - {next_time.strftime("%H:%M")}'
            )

            free_intervals[intervalstr] = available

            current_time = next_time

    this_day = date_now.date() == avail_day_date

    if this_day:
        current_hour_min = datetime.datetime.strptime(
            date_now.time().isoformat()[0:5], "%H:%M"
        )
        for finterval in free_intervals:
            fitime = datetime.datetime.strptime(finterval[0:5], "%H:%M")
            if current_hour_min >= fitime:
                free_intervals[finterval] = False

    return free_intervals


def get_service_object(sitedata: SiteDataModel, service_slug: str):
    service = None
    for s in sitedata.services:
        if s.slug_name == service_slug:
            service = s
            break
    return service


def get_interval_frame(service: BizzServiceModel):
    if service.time_unit == TIMEUNIT.HOURS:
        return datetime.timedelta(hours=service.time_value)
    return datetime.timedelta(minutes=service.time_value)


def add_already_set_appointments(
    free_intervals: dict,
    appointments: list[SetAppointmentModel],
    compare_avail_day: datetime.datetime,
):
    pop_intervals = set()
    for hour_interval, _ in free_intervals.items():
        for apomt in appointments:
            apomt_date = datetime.datetime.fromisoformat(apomt.time_start).date()
            if apomt_date == compare_avail_day:
                # hour_interval = "09:30 - 10:00"
                current_start_time = datetime.datetime.strptime(
                    hour_interval[:5], "%H:%M"
                )
                current_stop_time = datetime.datetime.strptime(
                    hour_interval[8:], "%H:%M"
                )

                # '2024-01-24T08:00:00.000000'
                start_time = datetime.datetime.strptime(
                    apomt.time_start.split("T")[1][:5], "%H:%M"
                )
                stop_time = datetime.datetime.strptime(
                    apomt.time_stop.split("T")[1][:5], "%H:%M"
                )

                # Check if overlaps
                if current_start_time < stop_time and start_time < current_stop_time:
                    pop_intervals.add(hour_interval)

    free_intervals = {
        hi: avail
        for hi, avail in free_intervals.items()
        if hi not in pop_intervals and avail
    }

    if not free_intervals:
        free_intervals = {"Inchis": False}

    return free_intervals


def fill_hour_ranges(
    date_now: datetime.datetime,
    availability: Availability,
    sitedata: SiteDataModel,
    daystr: str,
    interval: datetime.timedelta,
    weekstr: str,
):
    day_entries = getattr(sitedata.working_schedule, f"{daystr}_entries")
    week = getattr(availability, weekstr)
    avail_day = getattr(week, daystr)

    free_intervals = get_free_intervals(day_entries, interval, avail_day, date_now)

    if free_intervals:
        if availability.appointments is not None and avail_day.date is not None:
            free_intervals = add_already_set_appointments(
                free_intervals,
                availability.appointments,
                datetime.datetime.fromisoformat(avail_day.date).date(),
            )
        avail_day.entries = [
            Entry(hour_interval=hi, available=avail)
            for hi, avail in free_intervals.items()
            if avail
        ]

        if not avail_day.entries:
            avail_day.entries = [Entry(hour_interval="Inchis", available=False)]
    else:
        avail_day.entries = [Entry(hour_interval="Inchis")]

    return availability


def fill_working_hours(
    sitedata: SiteDataModel, availability: Availability, interval: datetime.timedelta
):
    date_now = datetime.datetime.fromisoformat(
        datetime.datetime.now(timezone("Europe/Bucharest")).isoformat()
    )

    daysstr = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    for daystr in daysstr:
        availability = fill_hour_ranges(
            date_now, availability, sitedata, daystr, interval, "current_week"
        )
        availability = fill_hour_ranges(
            date_now, availability, sitedata, daystr, interval, "next_week"
        )

    return availability


async def get_appointments_from_now_until_next_sunday(
    tenant_id: str, service: BizzServiceModel
):
    today = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    next_sunday = today + datetime.timedelta(days=(6 - today.weekday()) + 7)

    query = {
        "tenant_id": tenant_id,
        "canceled": False,
        "time_stop": {"$gte": today.isoformat(), "$lt": next_sunday.isoformat()},
    }

    programmed_appointments = await AppointmentCol.find_many(query)

    if not programmed_appointments:
        return None

    # Consider how many appointments the business can take in parallel
    programmed_appointments = [
        SetAppointmentModel(**pa) for pa in programmed_appointments
    ]

    ampt_for_service_count = len(
        [
            apmt
            for apmt in programmed_appointments
            if apmt.selected_service_slug == service.slug_name
        ]
    )

    if ampt_for_service_count < service.capacity:
        programmed_appointments = [
            apmt
            for apmt in programmed_appointments
            if apmt.selected_service_slug != service.slug_name
        ]

    return programmed_appointments


async def get_availability(tenant_id: str, service_slug: str):
    try:
        sitedata = await SiteDataCol.find_one({"tenant_id": tenant_id})
        sitedata = SiteDataModel(**sitedata)
        service = get_service_object(sitedata, service_slug)

        programmed_appointments = await get_appointments_from_now_until_next_sunday(
            tenant_id, service
        )
        availability = Availability(appointments=programmed_appointments)

        if sitedata.working_schedule is None or not service:
            return CustomResponse(
                content="Program de lucru", extra=availability.model_dump()
            )

        interval = get_interval_frame(service)
        availability = fill_working_hours(sitedata, availability, interval)

        return CustomResponse(
            content="Program de lucru", extra=availability.model_dump()
        )

    except Exception as err:
        log.exception(err)

    return CustomResponse(
        content="Nu am putut prelua programul de lucru. Incearca din nou.",
        status_code=500,
    )


async def appointment_made_but_not_confirmed_in_next_2_weeks(
    appointment_data: SetAppointmentModel,
):
    today = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    next_sunday = today + datetime.timedelta(days=(6 - today.weekday()) + 7)

    query = {
        "tenant_id": appointment_data.tenant_id,
        "confirmed": False,
        "canceled": False,
        "time_stop": {
            "$gte": today.isoformat(),
            "$lt": next_sunday.isoformat(),
        },
    }

    resp = CustomResponse(
        content="O programare a fost facuta deja de pe acest IP. Te vom contacta pentru confirmare cat de curand putem.",
        status_code=400,
    )

    if appointment_data.client_ip is not None:
        appointment_with_this_ip_made = await AppointmentCol.find_one(
            {**query, "client_ip": appointment_data.client_ip}
        )
        if appointment_with_this_ip_made:
            resp.extra = appointment_with_this_ip_made
            return resp

        appointment_with_this_phone_made = await AppointmentCol.find_one(
            {**query, "phone": appointment_data.phone}
        )
        if appointment_with_this_phone_made:
            resp.extra = appointment_with_this_phone_made
            return resp

    return None


async def get_service_from_service_slug(appointment_data: SetAppointmentModel):
    sitedata = await SiteDataCol.find_one({"tenant_id": appointment_data.tenant_id})

    if not sitedata:
        return

    sitedata = SiteDataModel(**sitedata)

    for service in sitedata.services:
        if appointment_data.selected_service_slug == service.slug_name:
            return service

    return


async def appointment_overlaps(
    appointment_data: SetAppointmentModel, service: BizzServiceModel
):
    try:
        apmts = await get_appointments_from_now_until_next_sunday(
            appointment_data.tenant_id, service
        )

        if not apmts:
            return

        current_tstart = datetime.datetime.fromisoformat(appointment_data.time_start)
        current_tstop = datetime.datetime.fromisoformat(appointment_data.time_stop)

        for apmt in apmts:
            given_tstart = datetime.datetime.fromisoformat(apmt.time_start)
            given_tstop = datetime.datetime.fromisoformat(apmt.time_stop)

            if current_tstart >= given_tstart and current_tstop <= given_tstop:
                return CustomResponse(
                    content="Exista deja o programare pentru acest interval",
                    status_code=400,
                )

    except Exception as err:
        log.exception(err)


async def set_appointment(client_ip: str, appointment_data: SetAppointmentModel):
    try:
        appointment_data.client_ip = (
            encrypt(client_ip) if client_ip is not None else None
        )

        service = await get_service_from_service_slug(appointment_data)
        if service is None:
            return CustomResponse(
                content="Serviciul selectat nu exista", status_code=404
            )

        appointment_data.selected_service_name = service.name

        resp = await appointment_made_but_not_confirmed_in_next_2_weeks(
            appointment_data
        )
        if resp is not None:
            return resp

        resp = await appointment_overlaps(appointment_data, service)
        if resp is not None:
            return resp

        inserted = await AppointmentCol.insert_one(appointment_data.model_dump())
        if inserted:
            return CustomResponse(
                content="Vei fi contactat pentru confirmare in cel mai scurt timp.",
                status_code=200,
                extra=appointment_data.appointment_id,
            )

    except Exception as err:
        log.exception(err)

    return CustomResponse(
        content="Nu am putut salva programarea. Incearca din nou.",
        status_code=500,
    )


async def get_active_appointment(tenant_id: str, appointment_id: str):
    try:
        data = await AppointmentCol.find_one(
            {
                "tenant_id": tenant_id,
                "appointment_id": appointment_id,
                "time_stop": {"$gte": datetime.datetime.now().isoformat()},
            }
        )

        if not data:
            return CustomResponse(
                content="Nici o programare online activa", status_code=404
            )

        return CustomResponse(content=data)

    except Exception as err:
        log.exception(err)

    return CustomResponse(
        content="Nu am putut gasi programarea",
        status_code=500,
    )


async def cancel_active_appointment(tenant_id: str, appointment_id: str):
    bad_resp = CustomResponse(
        content="Programarea online nu a putut fi anulata.", status_code=500
    )
    try:
        updated = await AppointmentCol.update_one(
            filters={"tenant_id": tenant_id, "appointment_id": appointment_id},
            data={"canceled": True},
        )

        if not updated:
            return bad_resp

        return CustomResponse(content=updated)

    except Exception as err:
        log.exception(err)

    return bad_resp


async def delete_old_appointments(tenant_id: str):
    today = datetime.datetime.today()

    return await AppointmentCol.delete_many(
        {
            "tenant_id": tenant_id,
            "$or": [
                {"time_stop": {"$lt": today.date().isoformat()}},
                {
                    "canceled": True,
                    "updated_at": {"$lt": today.date().isoformat()},
                },
            ],
        }
    )


async def get_active_appointments(tenant_id: str):
    bad_resp = CustomResponse(
        content="Nu au fost gasite noi programari pentru urmatoarele 2 saptamani.",
        status_code=500,
        extra=[],
    )
    try:
        today = datetime.datetime.today().replace(
            hour=0, minute=0, second=0, microsecond=0
        )

        admin_appointments = await AppointmentCol.find_many(
            filters={
                "tenant_id": tenant_id,
                "canceled": False,
                "day": {"$ne": None},
                "hour_interval": {"$ne": None},
                "selected_service_slug": {"$ne": None},
                "time_stop": {"$gte": today.isoformat()},
            },
            sort=[("time_start", 1)],
        )

        if not admin_appointments:
            return bad_resp

        # Mark today
        today = datetime.datetime.now().date()
        for apmt in admin_appointments:
            if datetime.datetime.fromisoformat(apmt["time_start"]).date() == today:
                apmt["day"] = "✨ " + apmt["day"]

        return CustomResponse(
            content="Programarile active pentru urmatoarele 2 saptamani au fost preluate",
            extra=admin_appointments,
        )

    except Exception as err:
        log.exception(err)

    return bad_resp


async def get_pending_appointments(tenant_id: str):
    bad_resp = CustomResponse(
        content="Nu au fost gasite noi programari pentru urmatoarele 2 saptamani.",
        status_code=500,
        extra=[],
    )
    try:
        admin_appointments = await AppointmentCol.find_many(
            filters={
                "tenant_id": tenant_id,
                "day": {"$eq": None},
                "hour_interval": {"$eq": None},
                "time_start": {"$eq": None},
                "time_stop": {"$eq": None},
            },
            sort=[("time_start", 1)],
        )

        if not admin_appointments:
            return bad_resp

        admin_appointments = [
            {**apmt, "day": "Nedefinit", "hour_interval": "Nedefinit"}
            for apmt in admin_appointments
        ]

        return CustomResponse(
            content="Programarile in asteptare pentru urmatoarele 2 saptamani au fost preluate",
            extra=admin_appointments,
        )

    except Exception as err:
        log.exception(err)

    return bad_resp


async def get_cancelled_appointments(tenant_id: str):
    bad_resp = CustomResponse(
        content="Nu au fost gasite noi programari pentru urmatoarele 2 saptamani.",
        status_code=500,
        extra=[],
    )
    try:
        today = datetime.datetime.today().replace(
            hour=0, minute=0, second=0, microsecond=0
        )

        admin_appointments = await AppointmentCol.find_many(
            filters={
                "tenant_id": tenant_id,
                "canceled": True,
                "time_stop": {"$gte": today.isoformat()},
            },
            sort=[("time_start", 1)],
        )

        if not admin_appointments:
            return bad_resp

        return CustomResponse(
            content="Programarile anulate pentru urmatoarele 2 saptamani au fost preluate",
            extra=admin_appointments,
        )

    except Exception as err:
        log.exception(err)

    return bad_resp


async def toggle_canceled_appointment(
    tenant_id: str, appointment_id: str, canceled: bool, owner: bool = False
):
    bad_resp = CustomResponse(
        content="Nu am putut executa acest request", status_code=500
    )
    try:
        updated = await AppointmentCol.update_one(
            filters={"tenant_id": tenant_id, "appointment_id": appointment_id},
            data={"canceled": canceled},
        )

        if not updated:
            return bad_resp

        return CustomResponse(content=updated)

    except Exception as err:
        log.exception(err)

    return bad_resp


async def toggle_confirmed_appointment(
    tenant_id: str, appointment_id: str, confirmed: bool
):
    bad_resp = CustomResponse(
        content="Nu am putut executa acest request.", status_code=500
    )
    try:
        updated = await AppointmentCol.update_one(
            filters={"tenant_id": tenant_id, "appointment_id": appointment_id},
            data={"confirmed": confirmed},
        )

        if not updated:
            return bad_resp

        return CustomResponse(content=updated)

    except Exception as err:
        log.exception(err)

    return bad_resp
