import re
import os
from config import cfg
from enum import StrEnum
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, model_validator
from common.save_image import save_image_sync
from common.utils import slugify
from .availability import Availability


ALLOWED_IMG_URLS = (
    "https://images.pexels.com",
    "https://images.unsplash.com",
    "https://img.freepik.com",
    "/public/crm/",
)


class TIMEUNIT(StrEnum):
    MINUTES = "minutes"
    HOURS = "hours"


class BizzServiceModel(BaseModel):
    id: Optional[int] = Field(default=1)
    name: str
    description: str
    picture: str
    slug_name: Optional[str] = None
    price: Optional[float] = None
    capacity: Optional[int] = Field(default=1)
    currency: Optional[str] = Field(default="RON")
    time_unit: Optional[TIMEUNIT] = Field(default=TIMEUNIT.MINUTES)
    time_value: Optional[int] = Field(default=30)

    @model_validator(mode="before")
    @classmethod
    def save_images_paths(cls, values: dict):
        # Save paths to db

        values["slug_name"] = slugify(values["name"])
        values["description"] = values["description"].strip()

        if values["picture"].startswith("/crm/images/"):
            filepath = f"{cfg.STORAGE_PATH}/crm/{os.path.basename(values['picture'])}"
            assert os.path.exists(filepath), "File doesn't exist."
            return values

        if re.search("data:image/.*;base64", values["picture"]):
            image_path = save_image_sync(values["picture"], "crm")
            values["picture"] = f"/crm/images/{os.path.basename(image_path)}"
            return values

        if values["picture"].startswith(ALLOWED_IMG_URLS):
            return values

        raise ValueError("Expected path, base64 or pexels image.")


class BizzTestimonial(BaseModel):
    id: Optional[int] = Field(default=1)
    person_name: Optional[str]
    occupation: Optional[str]
    testimonial: Optional[str]

    @staticmethod
    def fill_ids_for(testimonials: list["BizzTestimonial"], as_dict: bool = False):
        if as_dict:
            return [t.model_dump() for t in _add_ids(testimonials)]
        return _add_ids(testimonials)


class AnnouncementModel(BaseModel):
    message: str
    expire: str


class ExternalLinkModel(BaseModel):
    id: Optional[int] = Field(default=1)
    link: str
    name: str


class BizzType(StrEnum):
    AUTO = "SERVICE AUTO"
    DENTIST = "CABINET DENTAR"
    VETERINARY = "CABINET VETERINAR"
    SALON_BEAUTY = "SALON BEAUTY"
    BARBER_SHOP = "BARBER SHOP"
    TATOO = "TATUAJE"
    PSIHOLOG = "CABINET PSIHOLOGIC"
    OPTICA = "OPTICA MEDICALA"
    RECUPERARE_MEDICALA = "RECUPERARE MEDICALA"
    SITE_PREZENTARE = "WEBSITE + PROGRAMARI ONLINE"


class CTAModel(BaseModel):
    business_name: Optional[str] = None
    business_type: Optional[BizzType] = None
    main_cta: Optional[str] = None
    secondary_cta: Optional[str] = None
    picture_cta: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def save_images_paths(cls, values: dict):
        # Save paths to db

        if values["picture_cta"] is None:
            return values

        if values["picture_cta"].startswith("/crm/images/"):
            filepath = (
                f"{cfg.STORAGE_PATH}/crm/{os.path.basename(values['picture_cta'])}"
            )
            assert os.path.exists(filepath), "File doesn't exist."
            return values

        if re.search("data:image/.*;base64", values["picture_cta"]):
            image_path = save_image_sync(values["picture_cta"], "crm")
            values["picture_cta"] = f"/crm/images/{os.path.basename(image_path)}"
            return values

        if values["picture_cta"].startswith(ALLOWED_IMG_URLS):
            return values

        raise ValueError("Expected path, base64 or pexels image.")


class AboutModel(BaseModel):
    about_us: Optional[str] = None
    team_picture: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def save_images_paths(cls, values: dict):
        # Save paths to db

        if values["team_picture"].startswith("/crm/images/"):
            filepath = (
                f"{cfg.STORAGE_PATH}/crm/{os.path.basename(values['team_picture'])}"
            )
            assert os.path.exists(filepath), "File doesn't exist."
            return values

        if re.search("data:image/.*;base64", values["team_picture"]):
            image_path = save_image_sync(values["team_picture"], "crm")
            values["team_picture"] = f"/crm/images/{os.path.basename(image_path)}"
            return values

        if values["team_picture"].startswith(ALLOWED_IMG_URLS):
            return values

        raise ValueError("Expected path, base64 or pexels image.")


class ContactModel(BaseModel):
    google_maps_location_link: Optional[str] = None
    google_maps_location_picture: Optional[str] = None
    location_picture: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def save_images_paths(cls, values: dict):
        # Save paths to db

        if values["google_maps_location_picture"].startswith("/crm/images/"):
            filepath = f"{cfg.STORAGE_PATH}/crm/{os.path.basename(values['google_maps_location_picture'])}"
            assert os.path.exists(filepath), "File doesn't exist."
            return values

        if re.search("data:image/.*;base64", values["google_maps_location_picture"]):
            image_path = save_image_sync(values["google_maps_location_picture"], "crm")
            values[
                "google_maps_location_picture"
            ] = f"/crm/images/{os.path.basename(image_path)}"

        if values["location_picture"].startswith("/crm/images/"):
            filepath = (
                f"{cfg.STORAGE_PATH}/crm/{os.path.basename(values['location_picture'])}"
            )
            assert os.path.exists(filepath), "File doesn't exist."
            return values

        if re.search("data:image/.*;base64", values["location_picture"]):
            image_path = save_image_sync(values["location_picture"], "crm")
            values["location_picture"] = f"/crm/images/{os.path.basename(image_path)}"
            return values

        if values["google_maps_location_picture"].startswith(
            ALLOWED_IMG_URLS
        ) and values["location_picture"].startswith(ALLOWED_IMG_URLS):
            return values

        raise ValueError("Expected path, base64 or pexels image.")


class TimeFrameModel(BaseModel):
    id: Optional[int] = Field(default=1)
    start: Optional[str] = None
    stop: Optional[str] = None


class WorkingScheduleModel(BaseModel):
    monday_entries: Optional[list[TimeFrameModel]] = None
    tuesday_entries: Optional[list[TimeFrameModel]] = None
    wednesday_entries: Optional[list[TimeFrameModel]] = None
    thursday_entries: Optional[list[TimeFrameModel]] = None
    friday_entries: Optional[list[TimeFrameModel]] = None
    saturday_entries: Optional[list[TimeFrameModel]] = None
    sunday_entries: Optional[list[TimeFrameModel]] = None
    mentions: Optional[str] = None

    @model_validator(mode="after")
    @classmethod
    def validate(cls, wsm: "WorkingScheduleModel"):
        wsm.monday_entries = _validate_timeframes(wsm.monday_entries)
        wsm.tuesday_entries = _validate_timeframes(wsm.tuesday_entries)
        wsm.wednesday_entries = _validate_timeframes(wsm.wednesday_entries)
        wsm.thursday_entries = _validate_timeframes(wsm.thursday_entries)
        wsm.friday_entries = _validate_timeframes(wsm.friday_entries)
        wsm.saturday_entries = _validate_timeframes(wsm.saturday_entries)
        wsm.sunday_entries = _validate_timeframes(wsm.sunday_entries)

        return wsm


def _validate_timeframes(entries: list[TimeFrameModel] | None):
    if entries is None:
        return

    entries = [entry for entry in entries if entry.start and entry.stop]

    time_objects = []
    for entry in entries:
        time_objects.append(datetime.strptime(entry.start, "%H:%M"))
        time_objects.append(datetime.strptime(entry.stop, "%H:%M"))

    if sorted(time_objects) != time_objects:
        raise ValueError("Orele se suprapun")

    return entries if len(entries) > 0 else None


class SiteDataModel(BaseModel):
    tenant_id: Optional[str] = None
    announcement: Optional[AnnouncementModel] = None
    call_to_action: Optional[CTAModel] = None
    services: Optional[list[BizzServiceModel]] = None
    testimonials: Optional[list[BizzTestimonial]] = None
    about: Optional[AboutModel] = None
    contact: Optional[ContactModel] = None
    external_links: Optional[list[ExternalLinkModel]] = None
    working_schedule: Optional[WorkingScheduleModel] = None
    availability: Optional[Availability] = None
    updated_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())

    @model_validator(mode="after")
    @classmethod
    def set_ids(cls, values: "SiteDataModel"):
        values.services = _add_ids(values.services)

        if values.testimonials is not None:
            if len(values.testimonials) > 0:
                if values.testimonials[0].testimonial is None:
                    values.testimonials = None

        values.testimonials = _add_ids(
            values.testimonials if values.testimonials is not None else None
        )

        values.external_links = _add_ids(values.external_links)
        values.working_schedule.monday_entries = _add_ids(
            values.working_schedule.monday_entries
            if values.working_schedule is not None
            else None
        )
        values.working_schedule.tuesday_entries = _add_ids(
            values.working_schedule.tuesday_entries
            if values.working_schedule is not None
            else None
        )
        values.working_schedule.wednesday_entries = _add_ids(
            values.working_schedule.wednesday_entries
            if values.working_schedule is not None
            else None
        )
        values.working_schedule.thursday_entries = _add_ids(
            values.working_schedule.thursday_entries
            if values.working_schedule is not None
            else None
        )
        values.working_schedule.friday_entries = _add_ids(
            values.working_schedule.friday_entries
            if values.working_schedule is not None
            else None
        )
        values.working_schedule.saturday_entries = _add_ids(
            values.working_schedule.saturday_entries
            if values.working_schedule is not None
            else None
        )
        values.working_schedule.sunday_entries = _add_ids(
            values.working_schedule.sunday_entries
            if values.working_schedule is not None
            else None
        )
        return values


def _add_ids(items: list | None):
    if items is None:
        return items

    if not isinstance(items, list):
        return items

    items_with_ids = []
    for i, s in enumerate(items):
        s.id = i + 1
        items_with_ids.append(s)

    return items_with_ids
