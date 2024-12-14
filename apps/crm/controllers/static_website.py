from fastapi import APIRouter, Response, Cookie
from common.jwt import get_user_id_from_token
from typing import Annotated
from common.responses import CustomResponse
from apps.crm.models.sitedata import (
    AnnouncementModel,
    CTAModel,
    BizzServiceModel,
    AboutModel,
    BizzTestimonial,
    ContactModel,
    WorkingScheduleModel,
    ExternalLinkModel,
)
from apps.crm.views import static_website as staticView
from apps.crm.views import users as userView
from apps.crm.models.users import Roles


router = APIRouter(tags=["CRMSections"], prefix="/crm/static")


def user_not_authorized(user: dict | None):
    forbidden_resp = CustomResponse(content="Actiune neautorizata", status_code=403)

    if user is None:
        return forbidden_resp

    if user["role"] != Roles.ADMIN:
        return forbidden_resp

    return None


@router.post("/annoucement", response_model=CustomResponse)
async def save_annoucement(
    response: Response,
    annoucement: AnnouncementModel,
    token: Annotated[str | None, Cookie()] = None,
):
    user_id = await get_user_id_from_token(token)
    user = await userView.get_user_by_id(user_id)
    auth_resp = user_not_authorized(user)
    if auth_resp:
        response.status_code = auth_resp.status_code
        return auth_resp

    resp = await staticView.save_annoucement(user, annoucement)
    response.status_code = resp.status_code

    return resp


@router.post("/cta", response_model=CustomResponse)
async def save_cta(
    response: Response,
    cta: CTAModel,
    token: Annotated[str | None, Cookie()] = None,
):
    user_id = await get_user_id_from_token(token)
    user = await userView.get_user_by_id(user_id)

    auth_resp = user_not_authorized(user)
    if auth_resp:
        response.status_code = auth_resp.status_code
        return auth_resp

    resp = await staticView.save_cta(user, cta)
    response.status_code = resp.status_code

    return resp


@router.post("/services", response_model=CustomResponse)
async def save_services(
    response: Response,
    services: list[BizzServiceModel],
    token: Annotated[str | None, Cookie()] = None,
):
    user_id = await get_user_id_from_token(token)
    user = await userView.get_user_by_id(user_id)

    auth_resp = user_not_authorized(user)
    if auth_resp:
        response.status_code = auth_resp.status_code
        return auth_resp

    resp = await staticView.save_services(user, services)
    response.status_code = resp.status_code

    return resp


@router.post("/about", response_model=CustomResponse)
async def save_about(
    response: Response,
    about: AboutModel,
    token: Annotated[str | None, Cookie()] = None,
):
    user_id = await get_user_id_from_token(token)
    user = await userView.get_user_by_id(user_id)

    auth_resp = user_not_authorized(user)
    if auth_resp:
        response.status_code = auth_resp.status_code
        return auth_resp

    resp = await staticView.save_about(user, about)
    response.status_code = resp.status_code

    return resp


@router.post("/reviews", response_model=CustomResponse)
async def save_testimonials(
    response: Response,
    testimonials: list[BizzTestimonial],
    token: Annotated[str | None, Cookie()] = None,
):
    user_id = await get_user_id_from_token(token)
    user = await userView.get_user_by_id(user_id)

    auth_resp = user_not_authorized(user)
    if auth_resp:
        response.status_code = auth_resp.status_code
        return auth_resp

    resp = await staticView.save_testimonials(user, testimonials)
    response.status_code = resp.status_code

    return resp


@router.post("/contact", response_model=CustomResponse)
async def save_contact(
    response: Response,
    contact: ContactModel,
    token: Annotated[str | None, Cookie()] = None,
):
    user_id = await get_user_id_from_token(token)
    user = await userView.get_user_by_id(user_id)

    auth_resp = user_not_authorized(user)
    if auth_resp:
        response.status_code = auth_resp.status_code
        return auth_resp

    resp = await staticView.save_contact(user, contact)
    response.status_code = resp.status_code

    return resp


@router.post("/schedule", response_model=CustomResponse)
async def save_working_schedule(
    response: Response,
    schedule: WorkingScheduleModel,
    token: Annotated[str | None, Cookie()] = None,
):
    user_id = await get_user_id_from_token(token)
    user = await userView.get_user_by_id(user_id)

    auth_resp = user_not_authorized(user)
    if auth_resp:
        response.status_code = auth_resp.status_code
        return auth_resp

    resp = await staticView.save_working_schedule(user, schedule)
    response.status_code = resp.status_code

    return resp


@router.post("/external-links", response_model=CustomResponse)
async def save_external_links(
    response: Response,
    links: list[ExternalLinkModel],
    token: Annotated[str | None, Cookie()] = None,
):
    user_id = await get_user_id_from_token(token)
    user = await userView.get_user_by_id(user_id)

    auth_resp = user_not_authorized(user)
    if auth_resp:
        response.status_code = auth_resp.status_code
        return auth_resp

    resp = await staticView.save_external_links(user, links)
    response.status_code = resp.status_code

    return resp
