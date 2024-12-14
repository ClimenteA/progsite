from typing import Optional
from datetime import datetime, timedelta
from pydantic import BaseModel, Field, model_validator
from .constants import RO_DAYS, RO_MONTHS
from .appointment import SetAppointmentModel


class Entry(BaseModel):
    hour_interval: str = Field(default="Inchis")  # ex: "Inchis" | "08:00 - 08:45"
    available: bool = Field(default=False)


class DayEntry(BaseModel):
    day: Optional[str] = None  # ex: "Luni 15 Ian."
    date: Optional[str] = None  # utc isoformat date
    entries: list[Entry] = Field(default=[Entry()])


class DaysEntries(BaseModel):
    monday: DayEntry = Field(default=DayEntry())
    tuesday: DayEntry = Field(default=DayEntry())
    wednesday: DayEntry = Field(default=DayEntry())
    thursday: DayEntry = Field(default=DayEntry())
    friday: DayEntry = Field(default=DayEntry())
    saturday: DayEntry = Field(default=DayEntry())
    sunday: DayEntry = Field(default=DayEntry())


def get_current_week_dates():
    today = datetime.today()
    year, week_num, day_of_week = today.isocalendar()
    week_start = today - timedelta(days=day_of_week - 1)
    week_dates = [week_start + timedelta(days=i) for i in range(7)]
    return week_dates


def get_next_week_dates():
    today = datetime.today()
    next_week = today + timedelta(days=7)
    next_monday = next_week - timedelta(days=next_week.weekday())
    week_dates = [next_monday + timedelta(days=i) for i in range(7)]
    return week_dates


class Availability(BaseModel):
    current_week: DaysEntries = Field(default=DaysEntries())
    next_week: DaysEntries = Field(default=DaysEntries())
    appointments: Optional[list[SetAppointmentModel]] = None

    @model_validator(mode="after")
    @classmethod
    def fill_fields(cls, availability: "Availability"):
        current_weekday = datetime.today().weekday()

        cw = get_current_week_dates()

        availability.current_week.monday.date = cw[0].isoformat()
        availability.current_week.monday.day = f"{'✨ ' if current_weekday == cw[0].weekday() else ''}{RO_DAYS[cw[0].weekday()]} {cw[0].day} {RO_MONTHS[cw[0].month]}"

        availability.current_week.tuesday.date = cw[1].isoformat()
        availability.current_week.tuesday.day = f"{'✨ ' if current_weekday == cw[1].weekday() else ''}{RO_DAYS[cw[1].weekday()]} {cw[1].day} {RO_MONTHS[cw[1].month]}"

        availability.current_week.wednesday.date = cw[2].isoformat()
        availability.current_week.wednesday.day = f"{'✨ ' if current_weekday == cw[2].weekday() else ''}{RO_DAYS[cw[2].weekday()]} {cw[2].day} {RO_MONTHS[cw[2].month]}"

        availability.current_week.thursday.date = cw[3].isoformat()
        availability.current_week.thursday.day = f"{'✨ ' if current_weekday == cw[3].weekday() else ''}{RO_DAYS[cw[3].weekday()]} {cw[3].day} {RO_MONTHS[cw[3].month]}"

        availability.current_week.friday.date = cw[4].isoformat()
        availability.current_week.friday.day = f"{'✨ ' if current_weekday == cw[4].weekday() else ''}{RO_DAYS[cw[4].weekday()]} {cw[4].day} {RO_MONTHS[cw[4].month]}"

        availability.current_week.saturday.date = cw[5].isoformat()
        availability.current_week.saturday.day = f"{'✨ ' if current_weekday == cw[5].weekday() else ''}{RO_DAYS[cw[5].weekday()]} {cw[5].day} {RO_MONTHS[cw[5].month]}"
        availability.current_week.sunday.day = f"{'✨ ' if current_weekday == cw[6].weekday() else ''}{RO_DAYS[cw[6].weekday()]} {cw[6].day} {RO_MONTHS[cw[6].month]}"

        nw = get_next_week_dates()

        availability.next_week.monday.date = nw[0].isoformat()
        availability.next_week.monday.day = (
            f"{RO_DAYS[nw[0].weekday()]} {nw[0].day} {RO_MONTHS[nw[0].month]}"
        )

        availability.next_week.tuesday.date = nw[1].isoformat()
        availability.next_week.tuesday.day = (
            f"{RO_DAYS[nw[1].weekday()]} {nw[1].day} {RO_MONTHS[nw[1].month]}"
        )

        availability.next_week.wednesday.date = nw[2].isoformat()
        availability.next_week.wednesday.day = (
            f"{RO_DAYS[nw[2].weekday()]} {nw[2].day} {RO_MONTHS[nw[2].month]}"
        )

        availability.next_week.thursday.date = nw[3].isoformat()
        availability.next_week.thursday.day = (
            f"{RO_DAYS[nw[3].weekday()]} {nw[3].day} {RO_MONTHS[nw[3].month]}"
        )

        availability.next_week.friday.date = nw[4].isoformat()
        availability.next_week.friday.day = (
            f"{RO_DAYS[nw[4].weekday()]} {nw[4].day} {RO_MONTHS[nw[4].month]}"
        )

        availability.next_week.saturday.date = nw[5].isoformat()
        availability.next_week.saturday.day = (
            f"{RO_DAYS[nw[5].weekday()]} {nw[5].day} {RO_MONTHS[nw[5].month]}"
        )

        availability.next_week.sunday.date = nw[6].isoformat()
        availability.next_week.sunday.day = (
            f"{RO_DAYS[nw[6].weekday()]} {nw[6].day} {RO_MONTHS[nw[6].month]}"
        )

        return availability
