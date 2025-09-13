from fastapi import APIRouter, Depends
from dependencies import get_users_repository
from api.controllers.users import UsersController
from domain.users.repository import IUsersRepository
from domain.users.schema import (
    UserCreate,
    UserListResponse,
    UserResponse
)

router = APIRouter(prefix="/v1/users", tags=["users"])

def get_controller(repository: IUsersRepository = Depends(get_users_repository)):
    return UsersController(repository)


@router.get("/", summary="List users")
async def index(
    filter_params: str | None = None, 
    controller: UsersController = Depends(get_controller)
):
    return await controller.index(filter_params)

@router.post("/", summary="Create user")
async def create(user_param, controller: UsersController = Depends(get_controller)):
    return await controller.create(user_param)

@router.get("/{user_id}", summary="Get user details")
async def show(user_id: str, controller: UsersController = Depends(get_controller)) -> UserResponse:
    return await controller.show(user_id)
