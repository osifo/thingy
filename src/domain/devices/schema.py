from pydantic import BaseModel, Field
from domain.users.schema import User

class DeviceCreate(BaseModel):
    name: str = Field(min_length=2)
    description: str | None
    is_active: bool = False

class Device(DeviceCreate):
    id: str
    slug: str
    user: User

class DeviceCreateResponse(DeviceCreate):
    success: bool
    data: Device


class DeviceResponse(DeviceCreate):
    success: bool
    data: Device

class DeviceListResponse(DeviceCreate):
    success: bool
    data: list[Device]

    class Config:
        from_attributes = True
