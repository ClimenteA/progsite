from apps.crm.models.sitedata import (
    AnnouncementModel,
    SiteDataModel,
    CTAModel,
    BizzServiceModel,
    AboutModel,
    BizzTestimonial,
    ContactModel,
    WorkingScheduleModel,
    ExternalLinkModel,
)
from apps.crm.models.collections import SiteDataCol
from common.responses import CustomResponse, State
from common.logger import log


async def save_annoucement(user: dict, annoucement: AnnouncementModel):
    try:
        saveddata = await SiteDataCol.find_one({"tenant_id": user["tenant_id"]})

        if not saveddata:
            data = SiteDataModel(tenant_id=user["tenant_id"], announcement=annoucement)
            inserted = await SiteDataCol.insert_one(data.model_dump())
            if inserted:
                return CustomResponse(content="Anuntul a fost salvat")

        updated = await SiteDataCol.update_one(
            filters={"tenant_id": user["tenant_id"]},
            data={
                "announcement": annoucement.model_dump()
                if annoucement.message
                else None
            },
        )
        if updated:
            return CustomResponse(content="Anuntul a fost salvat")

    except Exception as err:
        log.exception(err)

    return CustomResponse(
        content="Nu am putut salva anuntul. Incearca din nou.",
        status=State.FAILED,
        status_code=500,
    )


async def save_cta(user: dict, cta: CTAModel):
    try:
        saveddata = await SiteDataCol.find_one({"tenant_id": user["tenant_id"]})

        if not saveddata:
            data = SiteDataModel(tenant_id=user["tenant_id"], call_to_action=cta)
            inserted = await SiteDataCol.insert_one(data.model_dump())
            if inserted:
                return CustomResponse(content="CTA a fost salvat")

        updated = await SiteDataCol.update_one(
            filters={"tenant_id": user["tenant_id"]},
            data={"call_to_action": cta.model_dump()},
        )
        if updated:
            return CustomResponse(content="CTA a fost actualizat")

    except Exception as err:
        log.exception(err)

    return CustomResponse(
        content="Nu am putut salva CTA. Incearca din nou.",
        status=State.FAILED,
        status_code=500,
    )


async def save_services(user: dict, services: list[BizzServiceModel]):
    try:
        saveddata = await SiteDataCol.find_one({"tenant_id": user["tenant_id"]})

        if not saveddata:
            data = SiteDataModel(tenant_id=user["tenant_id"], services=services)
            inserted = await SiteDataCol.insert_one(data.model_dump())
            if inserted:
                return CustomResponse(content="Serviciile au fost salvate")

        updated = await SiteDataCol.update_one(
            filters={"tenant_id": user["tenant_id"]},
            data={"services": [s.model_dump() for s in services]},
        )
        if updated:
            return CustomResponse(content="Serviciile au fost salvate")

    except Exception as err:
        log.exception(err)

    return CustomResponse(
        content="Nu am putut salva serviciile. Incearca din nou.",
        status=State.FAILED,
        status_code=500,
    )


async def save_about(user: dict, about: AboutModel):
    try:
        saveddata = await SiteDataCol.find_one({"tenant_id": user["tenant_id"]})

        if not saveddata:
            data = SiteDataModel(tenant_id=user["tenant_id"], about=about)
            inserted = await SiteDataCol.insert_one(data.model_dump())
            if inserted:
                return CustomResponse(content="Sectiunea despre noi a fost salvata")

        updated = await SiteDataCol.update_one(
            filters={"tenant_id": user["tenant_id"]},
            data={"about": about.model_dump()},
        )
        if updated:
            return CustomResponse(content="Sectiunea despre noi a fost salvata")

    except Exception as err:
        log.exception(err)

    return CustomResponse(
        content="Nu am putut salva sectiunea despre noi. Incearca din nou.",
        status=State.FAILED,
        status_code=500,
    )


async def save_testimonials(user: dict, testimonials: list[BizzTestimonial]):
    try:
        saveddata = await SiteDataCol.find_one({"tenant_id": user["tenant_id"]})

        if not saveddata:
            data = SiteDataModel(tenant_id=user["tenant_id"], testimonials=testimonials)
            inserted = await SiteDataCol.insert_one(data.model_dump())
            if inserted:
                return CustomResponse(content="Testimonialele au fost salvate")

        if len(testimonials) > 0:
            if testimonials[0].testimonial is None:
                updated = await SiteDataCol.update_one(
                    filters={"tenant_id": user["tenant_id"]},
                    data={"testimonials": None},
                )
                if updated:
                    return CustomResponse(content="Testimonialele au fost sterse")

        updated = await SiteDataCol.update_one(
            filters={"tenant_id": user["tenant_id"]},
            data={
                "testimonials": BizzTestimonial.fill_ids_for(testimonials, as_dict=True)
            },
        )
        if updated:
            return CustomResponse(content="Testimonialele au fost salvate")

    except Exception as err:
        log.exception(err)

    return CustomResponse(
        content="Nu am putut salva testimonialele. Incearca din nou.",
        status=State.FAILED,
        status_code=500,
    )


async def save_contact(user: dict, contact: ContactModel):
    try:
        saveddata = await SiteDataCol.find_one({"tenant_id": user["tenant_id"]})

        if not saveddata:
            data = SiteDataModel(tenant_id=user["tenant_id"], contact=contact)
            inserted = await SiteDataCol.insert_one(data.model_dump())
            if inserted:
                return CustomResponse(content="Sectiunea contact a fost salvata")

        updated = await SiteDataCol.update_one(
            filters={"tenant_id": user["tenant_id"]},
            data={"contact": contact.model_dump()},
        )
        if updated:
            return CustomResponse(content="Sectiunea contact a fost salvata")

    except Exception as err:
        log.exception(err)

    return CustomResponse(
        content="Nu am putut salva sectiunea contact. Incearca din nou.",
        status=State.FAILED,
        status_code=500,
    )


async def save_working_schedule(user: dict, schedule: WorkingScheduleModel):
    try:
        saveddata = await SiteDataCol.find_one({"tenant_id": user["tenant_id"]})

        if not saveddata:
            data = SiteDataModel(tenant_id=user["tenant_id"], working_schedule=schedule)
            inserted = await SiteDataCol.insert_one(data.model_dump())
            if inserted:
                return CustomResponse(
                    content="Sectiunea program de lucru a fost salvata"
                )

        updated = await SiteDataCol.update_one(
            filters={"tenant_id": user["tenant_id"]},
            data={"working_schedule": schedule.model_dump()},
        )
        if updated:
            return CustomResponse(content="Sectiunea program de lucru a fost salvata")

    except Exception as err:
        log.exception(err)

    return CustomResponse(
        content="Nu am putut salva sectiunea program de lucru. Incearca din nou.",
        status=State.FAILED,
        status_code=500,
    )


async def save_external_links(user: dict, links: list[ExternalLinkModel]):
    try:
        saveddata = await SiteDataCol.find_one({"tenant_id": user["tenant_id"]})

        if not saveddata:
            data = SiteDataModel(tenant_id=user["tenant_id"], external_links=links)
            inserted = await SiteDataCol.insert_one(data.model_dump())
            if inserted:
                return CustomResponse(content="Link-urile externe au fost salvate.")

        updated = await SiteDataCol.update_one(
            filters={"tenant_id": user["tenant_id"]},
            data={"external_links": [link.model_dump() for link in links]},
        )
        if updated:
            return CustomResponse(content="Link-urile externe au fost salvate.")

    except Exception as err:
        log.exception(err)

    return CustomResponse(
        content="Link-urile externe nu au fost salvate. Incearca din nou.",
        status=State.FAILED,
        status_code=500,
    )
