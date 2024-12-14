from typing import Annotated
from fastapi import APIRouter, Request, Cookie
from fastapi.responses import Response
from apps.crm.models import appointment as AppoinmentModel
from apps.crm.views import appointment as AppoitmentsView
from common.responses import CustomResponse
from common.jwt import get_user_id_from_token
from apps.crm.views import users as userView


router = APIRouter(tags=["CRMAppointments"], prefix="/crm/appointments")


@router.get("/{tenant_id}/{service_slug}", response_model=CustomResponse)
async def crm_get_availability(response: Response, tenant_id: str, service_slug: str):
    resp = await AppoitmentsView.get_availability(tenant_id, service_slug)
    response.status_code = resp.status_code
    return resp


@router.post("/set", response_model=CustomResponse)
async def crm_set_appointment(
    request: Request,
    response: Response,
    appointment_data: AppoinmentModel.SetAppointmentModel,
    token: Annotated[str | None, Cookie()] = None,
):
    user_id = await get_user_id_from_token(token)
    user = await userView.get_user_by_id(user_id)
    if user is None:
        client_ip = request.client.host
        appointment_data.confirmed = False
        resp = await AppoitmentsView.set_appointment(client_ip, appointment_data)
        response.status_code = resp.status_code
        return resp

    if user["tenant_id"] != appointment_data.tenant_id:
        return CustomResponse(content="Actiune neautorizata", status_code=403)

    appointment_data.confirmed = True if appointment_data.hour_interval else False
    resp = await AppoitmentsView.set_appointment(None, appointment_data)
    response.status_code = resp.status_code
    return resp


@router.get("/active/{tenant_id}/{appointment_id}", response_model=CustomResponse)
async def crm_get_active_appointment(
    response: Response,
    tenant_id: str,
    appointment_id: str,
    token: Annotated[str | None, Cookie()] = None,
):
    user_id = await get_user_id_from_token(token)
    user = await userView.get_user_by_id(user_id)
    if user:
        return CustomResponse(
            content="Adminii nu pot avea programari active", status_code=400
        )

    resp = await AppoitmentsView.get_active_appointment(tenant_id, appointment_id)
    response.status_code = resp.status_code
    return resp


@router.put("/cancel/{tenant_id}/{appointment_id}", response_model=CustomResponse)
async def crm_cancel_active_appointment(
    response: Response, tenant_id: str, appointment_id: str
):
    resp = await AppoitmentsView.cancel_active_appointment(tenant_id, appointment_id)
    response.status_code = resp.status_code
    return resp


@router.post(
    "/toggle-canceled/{tenant_id}/{appointment_id}/{canceled}",
    response_model=CustomResponse,
)
async def crm_toggle_active_appointment(
    response: Response,
    tenant_id: str,
    appointment_id: str,
    canceled: str,
    token: Annotated[str | None, Cookie()] = None,
):
    user_id = await get_user_id_from_token(token)
    user = await userView.get_user_by_id(user_id)
    if user is None:
        return CustomResponse(content="Neautorizat", status_code=403)

    owner = tenant_id == user["tenant_id"]
    if not owner:
        return CustomResponse(content="Neautorizat", status_code=403)

    canceled = True if canceled == "true" else False

    resp = await AppoitmentsView.toggle_canceled_appointment(
        tenant_id, appointment_id, canceled, owner
    )
    response.status_code = resp.status_code
    return resp


@router.post(
    "/toggle-confirmed/{tenant_id}/{appointment_id}/{confirmed}",
    response_model=CustomResponse,
)
async def crm_toggle_confirmed_appointment(
    response: Response,
    tenant_id: str,
    appointment_id: str,
    confirmed: str,
    token: Annotated[str | None, Cookie()] = None,
):
    user_id = await get_user_id_from_token(token)
    user = await userView.get_user_by_id(user_id)
    if user is None:
        return CustomResponse(content="Neautorizat", status_code=403)

    if tenant_id != user["tenant_id"]:
        return CustomResponse(content="Neautorizat", status_code=403)

    confirmed = True if confirmed == "true" else False

    resp = await AppoitmentsView.toggle_confirmed_appointment(
        tenant_id, appointment_id, confirmed
    )
    response.status_code = resp.status_code
    return resp
