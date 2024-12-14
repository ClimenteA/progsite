from apps.crm.demo.landing_demo import landing_site_data
from apps.crm.models.users import UserModel, Roles
from apps.crm.views.users import register_user
from common.responses import State
from config import cfg
from apps.crm.models.collections import UsersCol


async def create_admin_account():
    user = await UsersCol.find_one({"email": cfg.ADMIN_EMAIL})
    if user:
        return user["tenant_id"]

    registered = await register_user(
        user=UserModel(
            username=cfg.ADMIN_USERNAME,
            password=cfg.ADMIN_PASSWORD,
            phone="0711111111",
            email=cfg.ADMIN_EMAIL,
            role=Roles.ADMIN,
            verified=True,
        ),
        default_site_data=landing_site_data,
    )
    if registered.status == State.SUCCESS:
        return registered.extra

    raise Exception("Cannot create admin user!")
