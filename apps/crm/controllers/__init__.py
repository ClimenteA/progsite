from .landing import router as LandingR
from .users import router as UserR
from .static_website import router as StaticR
from .appointment import router as AppointmentR

routers = [LandingR, UserR, StaticR, AppointmentR]
