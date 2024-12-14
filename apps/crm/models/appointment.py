import re
import uuid
import datetime
from typing import Optional

from common.logger import log
from .constants import RO_MONTHS_R
from pydantic import BaseModel, Field, model_validator


class SetAppointmentModel(BaseModel):
    appointment_id: Optional[str] = Field(default_factory=lambda: uuid.uuid4().hex)
    tenant_id: str
    full_name: str
    day: Optional[str] = None
    hour_interval: Optional[str] = None
    selected_service_name: Optional[str] = None
    selected_service_slug: str
    phone: str
    message: Optional[str] = Field(max_length=1000, default=None)
    time_start: Optional[str] = None
    time_stop: Optional[str] = None
    confirmed: Optional[bool] = False
    canceled: Optional[bool] = False
    client_ip: Optional[str] = None
    updated_at: Optional[str] = Field(
        default_factory=lambda: datetime.datetime.utcnow().isoformat()
    )

    @model_validator(mode="after")
    @classmethod
    def validate_and_fill_fields(cls, sapmt: "SetAppointmentModel"):
        assert (
            sapmt.phone.startswith("07")
            and len(sapmt.phone) == 10
            and sapmt.phone.isdigit()
        ), "Numar telefon invalid"

        if sapmt.day == "Nedefinita" or sapmt.hour_interval == "Nedefinita":
            sapmt.day = None
            sapmt.hour_interval = None
            return sapmt

        try:
            current_year = datetime.datetime.now().year

            # "Vineri 2 Feb"
            sapmt.day = sapmt.day.replace("✨", "").strip()
            month_day = re.search(r".*\s(\d{1,2})\s.*", sapmt.day).group(1)
            short_month = re.search(r".*\s\d{1,2}\s(.*)", sapmt.day).group(1)
            month_str = f"{RO_MONTHS_R[short_month]:02d}"
            month_day = f"{int(month_day):02d}"

            # "09:30 - 10:00"
            hour_start_str = sapmt.hour_interval[:5]
            hour_end_str = sapmt.hour_interval[8:]

            timstamp_start = (
                f"{current_year}-{month_str}-{month_day}T{hour_start_str}:00.000000"
            )
            timstamp_end = (
                f"{current_year}-{month_str}-{month_day}T{hour_end_str}:00.000000"
            )

            sapmt.time_start = datetime.datetime.fromisoformat(
                timstamp_start
            ).isoformat()

            sapmt.time_stop = datetime.datetime.fromisoformat(timstamp_end).isoformat()

        except Exception as err:
            log.exception(err)
            raise Exception("Nu am putut interpreta datele primite")

        return sapmt
