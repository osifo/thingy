from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime
class UserCreate(BaseModel):
    email: EmailStr
    firstname: str
    lastname: str
    age: int | None = None
    username: str = Field(min_length=3)

class User(UserCreate):
    id: str
    # is_active: bool
    # last_active_date: str
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

class UserResponse(BaseModel):
    success: bool
    data: User

class UserListResponse(BaseModel):
    success: bool
    data: list[User]
