import os
from apps.crm.models.users import Roles
from config import cfg
from fastapi import APIRouter, Request, Cookie
from fastapi.responses import HTMLResponse, FileResponse
from common.render_template import render_template
from apps.crm.demo import demo_sites_mapper
from fastapi.responses import RedirectResponse
from common.jwt import get_user_id_from_token
from typing import Annotated
from apps.crm.views import users as userView
from apps.crm.views.admin import create_admin_account
from apps.crm.views import appointment as ApmtView

router = APIRouter(tags=["CRMLanding"], prefix="/crm")


@router.get("/images/{image_name}", response_class=FileResponse)
async def crm_get_image_from_storage(image_name: str):
    filepath = f"{cfg.STORAGE_PATH}/crm/{image_name}"

    if os.path.exists(filepath):
        return FileResponse(filepath, status_code=200)

    return FileResponse("./public/notimg.svg", status_code=404)


@router.get("/dashboard", response_class=HTMLResponse)
async def crm_dashboard_template(
    request: Request,
    token: Annotated[str | None, Cookie()] = None,
):
    user_id = await get_user_id_from_token(token)
    user = await userView.get_user_by_id(user_id)
    if user is None:
        return RedirectResponse("/crm/users/login")

    sitedata = await userView.get_user_site_data(user["tenant_id"])

    invited_users = []
    if user["role"] == Roles.ADMIN:
        invited_users = await userView.get_invited_users(user["tenant_id"])

    await ApmtView.delete_old_appointments(user["tenant_id"])

    active_apmt = await ApmtView.get_active_appointments(user["tenant_id"])
    pending_apmt = await ApmtView.get_pending_appointments(user["tenant_id"])
    cancelled_apmt = await ApmtView.get_cancelled_appointments(user["tenant_id"])

    return await render_template(
        request,
        "crm/dashboard_template.html",
        context={
            "user": user,
            "data": sitedata,
            "invited_users": invited_users,
            "active_appointments": active_apmt.extra,
            "pending_appointments": pending_apmt.extra,
            "cancelled_appointments": cancelled_apmt.extra,
        },
    )


@router.get("/landing", response_class=HTMLResponse)
async def crm_get_landing_template():
    tenant_id = await create_admin_account()
    return RedirectResponse(f"/crm/website/{tenant_id}")


@router.get("/site-demo/{site_type}", response_class=HTMLResponse)
async def crm_get_site_demo_template(request: Request, site_type: str):
    if site_type not in demo_sites_mapper:
        return RedirectResponse("/", status_code=302)
    return await render_template(
        request,
        "crm/site_template.html",
        context={"demo": True, "data": demo_sites_mapper[site_type]},
    )


@router.get("/website/{tenant_id}", response_class=HTMLResponse)
async def crm_get_tenant_website_template(
    request: Request,
    tenant_id: str,
    token: Annotated[str | None, Cookie()] = None,
):
    sitedata = await userView.get_user_site_data(tenant_id)
    user_id = await get_user_id_from_token(token)
    user = await userView.get_user_by_id(user_id)
    return await render_template(
        request,
        "crm/site_template.html",
        context={"demo": False, "user": user, "data": sitedata},
    )
