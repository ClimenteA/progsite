import datetime
from common.responses import CustomResponse, State
from common.logger import log
from common.password import encrypt
from apps.crm.models import users as userModel
from apps.crm.models.sitedata import SiteDataModel
from apps.crm.models.collections import UsersCol, CRMCol, SiteDataCol
from common.jwt import get_token_for_user_id, blacklist_token
from apps.crm.demo.build_demo import build_site_data
from apps.crm.models.availability import Availability
from apps.crm.demo import demo_sites_mapper_ro


async def register_user(
    user: userModel.UserModel, default_site_data: SiteDataModel = build_site_data
):
    bad_resp = CustomResponse(
        content="Linkul de invitatie a expirat sau nu ai folosit emailul cu care ai fost invitat",
        status_code=400,
    )
    cant_create_account_resp = CustomResponse(
        content="Nu am putut crea contul. Incearca din nou.",
        status_code=500,
    )

    try:
        existing_user = await UsersCol.find_one({"email": user.email})

        if existing_user and user.invite_token is None:
            return CustomResponse(
                status=State.FAILED,
                content="Acest email este deja utilizat.",
                status_code=400,
            )

        if user.invite_token is not None and not existing_user:
            return bad_resp

        if user.invite_token is not None:
            date_30days_ago = datetime.datetime.utcnow() - datetime.timedelta(days=30)
            date_invited_on = datetime.datetime.fromisoformat(
                existing_user["invited_on"]
            )
            expired_token = date_invited_on < date_30days_ago
            if expired_token:
                await UsersCol.delete_one({"invite_token": user.invite_token})
                return bad_resp

        if user.invite_token is None:
            default_site_data = (
                demo_sites_mapper_ro.get(user.business_type)
                or default_site_data.model_dump()
            )

            sitedata = SiteDataModel(**default_site_data)
            sitedata.tenant_id = user.tenant_id
            inserted_default = await SiteDataCol.insert_one(sitedata.model_dump())
            if not inserted_default:
                return cant_create_account_resp
        else:
            user.role = existing_user["role"]
            user.tenant_id = existing_user["tenant_id"]
            user.verified = True

        user.password = encrypt(user.password)

        inserted_user = await UsersCol.insert_one(
            {**user.model_dump(), "invite_token": None, "active": True}
        )
        if inserted_user:
            if user.invite_token:
                await UsersCol.delete_one({"invite_token": user.invite_token})
            return CustomResponse(content="Contul a fost creat", extra=user.tenant_id)

        return cant_create_account_resp

    except Exception as err:
        log.exception(err)
        return cant_create_account_resp


async def login_user(creds: userModel.UserLoginModel):
    try:
        user = await UsersCol.find_one({"email": creds.phone_or_email})
        if not user:
            user = await UsersCol.find_one({"phone": creds.phone_or_email})

        bad_creds_response = CustomResponse(
            status=State.FAILED,
            content="Email/Telefon sau Parola incorecte.",
            status_code=400,
        )

        if not user:
            return bad_creds_response

        if user["password"] != encrypt(creds.password):
            return bad_creds_response

        token = await get_token_for_user_id(
            user["user_id"],
            users_col=CRMCol.Users,
            blacktoken_col=CRMCol.TokenBlackList,
        )

        return CustomResponse(content=token)

    except Exception as err:
        log.exception(err)
        return CustomResponse(
            content="Nu am putut crea contul. Incerca din nou.", status_code=500
        )


async def logout(token: str | None):
    blacklisted = await blacklist_token(token)
    if blacklisted:
        return CustomResponse(content="Token blacklisted")
    return CustomResponse(
        content="Invalid token",
        status=State.FAILED,
        status_code=400,
    )


async def get_user_by_id(user_id: str | None):
    try:
        if user_id is None:
            return
        user = await UsersCol.find_one(filters={"user_id": user_id})
        if user:
            return user
    except Exception as err:
        log.exception(err)
    return None


async def get_user_site_data(tenant_id: str):
    try:
        sitedata = await SiteDataCol.find_one({"tenant_id": tenant_id})

        if sitedata["announcement"] is not None:
            if datetime.datetime.now() >= datetime.datetime.fromisoformat(
                sitedata["announcement"]["expire"]
            ):
                sitedata["announcement"] = None
                await SiteDataCol.update_one(
                    filters={"tenant_id": tenant_id}, data={"announcement": None}
                )

        sitedata["availability"] = Availability().model_dump()
        return sitedata
    except Exception as err:
        log.exception(err)
    return None


async def invite_user(invited_user: userModel.InviteUserModel):
    try:
        user_exists = await UsersCol.find_one(
            filters={"tenant_id": invited_user.tenant_id, "email": invited_user.email}
        )

        if user_exists:
            return CustomResponse(
                content="Utilizatorul a mai fost invitat. Sterge utilizatorul inainte de aceasta operatie.",
                status_code=400,
            )

        user = userModel.UserModel(
            tenant_id=invited_user.tenant_id,
            username=invited_user.email.split("@")[0],
            password="TEMPORARY INVITED USER",
            phone="0700000000",
            email=invited_user.email,
            role=invited_user.role,
            active=False,
            invite_token=invited_user.invite_token,
            invited_on=datetime.datetime.utcnow().isoformat(),
            verified=True,
        )

        inserted_user = await UsersCol.insert_one(user.model_dump())
        if inserted_user:
            return CustomResponse(
                content="Contul temporar a fost creat. Trimite linkul de invitatie catre persoana invitata.",
                extra=invited_user.invite_token,
            )

        return CustomResponse(
            content="Nu am putut crea contul. Incearca din nou.",
            status_code=500,
        )

    except Exception as err:
        log.exception(err)

    return CustomResponse(
        content="Nu am putut crea linkul. Asigura-te ca emailul este valid.",
        status_code=500,
    )


async def get_invited_users(tenant_id: str):
    try:
        users = await UsersCol.find_many(
            {"tenant_id": tenant_id, "user_id": {"$ne": tenant_id}}
        )
        return users
    except Exception as err:
        log.exception(err)
    return []


async def toggle_active_user_status(user_id: str, active_status: bool):
    try:
        updated = await UsersCol.update_one(
            filters={"user_id": user_id},
            data={"active": active_status},
        )
        if updated:
            return CustomResponse(content="Statusul utilizatorului a fost schimbat")
    except Exception as err:
        log.exception(err)
    return CustomResponse(content="Nu am putut schimba statusul", status_code=500)


async def delete_invited_user(user_id: str):
    try:
        deleted = await UsersCol.delete_one(filters={"user_id": user_id})
        if deleted:
            return CustomResponse(content="Utilizatorului a fost sters")
    except Exception as err:
        log.exception(err)
    return CustomResponse(content="Nu am putut sterge utilizatorul", status_code=500)
