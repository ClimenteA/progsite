import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, model_validator
from enum import StrEnum


class Roles(StrEnum):
    ADMIN = "admin"
    NORMAL = "normal"


class InviteUserModel(BaseModel):
    tenant_id: str
    email: str
    role: Roles
    invite_token: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def validate_fields(cls, values: dict):
        values["invite_token"] = uuid.uuid4().hex

        values["email"] = values["email"].lower()
        assert values["email"].count("@") == 1, "Invalid email"
        assert values["email"].count(".") >= 1, "Invalid email"

        return values


class UserLoginModel(BaseModel):
    phone_or_email: str
    password: str


class UserModel(BaseModel):
    user_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    tenant_id: Optional[str] = None
    username: str
    password: str
    phone: str
    email: str
    role: Optional[Roles] = Roles.ADMIN
    verified: Optional[bool] = False
    active: Optional[bool] = True
    invite_token: Optional[str] = None
    invited_on: Optional[str] = None
    business_type: Optional[str] = None
    last_login: str = Field(default_factory=lambda: datetime.utcnow().isoformat())

    @model_validator(mode="after")
    @classmethod
    def validate_fields(cls, values: "UserModel"):
        if values.tenant_id is None:
            values.tenant_id = values.user_id

        assert (
            len(values.password) >= 6
        ), "Password must be bigger or equal to 6 characters"

        values.email = values.email.lower()

        assert values.email.count("@") == 1, "Email invalid"
        assert values.email.count(".") >= 1, "Email invalid"

        assert len(values.phone) == 10, "Numar telefon invalid"
        assert values.phone.startswith("07"), "Numar telefon invalid"
        assert len(values.username) >= 3, "Numele trebuie sa aiba minim 3 caractere"

        return values
