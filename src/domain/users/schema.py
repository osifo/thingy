from pydantic import BaseModel, Field, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    firstname: str
    lastname: str
    age: int
    username: str = Field(min_length=3)

class User(UserCreate):
    id: str
    is_active: bool
    last_active_date: str

class UserCreateResponse(UserCreate):
    success: bool
    data: User

class UserResponse(User):
    success: bool
    data: User

class UserListResponse(User):
    success: bool
    data: list[User]

    class Config:
        from_attributes = True
