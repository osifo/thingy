from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict
from domain.users.schema import User

class DeviceCreate(BaseModel):
    name: str = Field(min_length=2)
    description: str | None
    is_active: bool = False

class Device(DeviceCreate):
    id: str
    slug: str
    user: User
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

class DeviceCreateResponse(BaseModel):
    success: bool
    data: Device


class DeviceResponse(BaseModel):
    success: bool
    data: Device

class DeviceListResponse(BaseModel):
    success: bool
    data: list[Device]

    class Config:
        from_attributes = True
