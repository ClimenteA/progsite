from typing import Annotated
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import APIRouter, Request, Cookie, Response
from common.render_template import render_template
from common.jwt import get_user_id_from_token
from apps.crm.models import users as userModel
from apps.crm.views import users as userView
from common.responses import CustomResponse
from apps.crm.models.users import Roles
from common.notifications import send_notification

router = APIRouter(tags=["CRMUsers"], prefix="/crm/users")


@router.get("/register", response_class=HTMLResponse)
async def get_register_template(
    request: Request,
    invite_token: str | None = None,
    token: Annotated[str | None, Cookie()] = None,
):
    user_id = await get_user_id_from_token(token)
    if user_id is not None:
        return RedirectResponse("/crm/dashboard")
    return await render_template(
        request, "crm/auth_register.html", context={"invite_token": invite_token}
    )


@router.get("/login", response_class=HTMLResponse)
async def get_login_template(
    request: Request,
    token: Annotated[str | None, Cookie()] = None,
):
    user_id = await get_user_id_from_token(token)
    if user_id is not None:
        return RedirectResponse("/crm/dashboard")
    return await render_template(request, "crm/auth_login.html")


@router.post("/register", response_model=CustomResponse)
async def post_register(
    response: Response,
    user: userModel.UserModel,
):
    resp = await userView.register_user(user)

    send_notification(
        title="progsite",
        message=f"New user on progsite.ro! Email: {user.email}",
    )

    response.status_code = resp.status_code
    return resp


@router.post("/login", response_model=CustomResponse)
async def post_login(response: Response, user: userModel.UserLoginModel):
    resp = await userView.login_user(user)
    response.status_code = resp.status_code
    response.set_cookie(key="token", value=resp.content)
    return resp


@router.get("/logout", response_model=CustomResponse)
async def get_logout(response: Response, token: Annotated[str | None, Cookie()] = None):
    resp = await userView.logout(token)
    response.delete_cookie(key="token")
    response.status_code = resp.status_code
    return RedirectResponse("/crm/users/login")


@router.post("/invite", response_model=CustomResponse)
async def post_invite_user(
    response: Response,
    invitedUser: userModel.InviteUserModel,
    token: Annotated[str | None, Cookie()] = None,
):
    user_id = await get_user_id_from_token(token)
    user = await userView.get_user_by_id(user_id)

    forbidden_resp = CustomResponse(content="Actiune neautorizata", status_code=403)

    if user is None:
        return forbidden_resp

    if user["tenant_id"] != invitedUser.tenant_id or user["role"] != Roles.ADMIN:
        return forbidden_resp

    resp = await userView.invite_user(invitedUser)
    response.status_code = resp.status_code
    return resp


@router.put(
    "/toggle-active-status/{required_user_id}/{active_status}",
    response_model=CustomResponse,
)
async def put_toggle_active_user_status(
    response: Response,
    required_user_id: str,
    active_status: str,
    token: Annotated[str | None, Cookie()] = None,
):
    user_id = await get_user_id_from_token(token)
    user = await userView.get_user_by_id(user_id)

    forbidden_resp = CustomResponse(content="Actiune neautorizata", status_code=403)

    if user is None:
        return forbidden_resp

    if user["role"] != Roles.ADMIN:
        return forbidden_resp

    active_status = True if active_status == "true" else False

    resp = await userView.toggle_active_user_status(required_user_id, active_status)
    response.status_code = resp.status_code
    return resp


@router.delete("/delete-invited-user/{required_user_id}", response_model=CustomResponse)
async def delete_invited_user(
    response: Response,
    required_user_id: str,
    token: Annotated[str | None, Cookie()] = None,
):
    user_id = await get_user_id_from_token(token)
    user = await userView.get_user_by_id(user_id)

    forbidden_resp = CustomResponse(content="Actiune neautorizata", status_code=403)

    if user is None:
        return forbidden_resp

    if user["role"] != Roles.ADMIN:
        return forbidden_resp

    resp = await userView.delete_invited_user(required_user_id)
    response.status_code = resp.status_code
    return resp
