from fastapi import APIRouter, Depends
from api.controllers.users import get_users_controller
from domain.users.schema import (
    UserCreate,
    UserListResponse,
    UserResponse
)

router = APIRouter(prefix="/v1/users", tags=["users"])

@router.get("/", summary="List users")
async def index(
    filter_params: str | None = None, 
    controller = Depends(get_users_controller)
):
    return await controller.index(filter_params)

@router.post("/", summary="Create user")
async def create(user_param, controller = Depends(get_users_controller)):
    return await controller.create(user_param)

@router.get("/{user_id}", summary="Get user details")
async def show(user_id: str, controller = Depends(get_users_controller)) -> UserResponse:
    return await controller.show(user_id)
