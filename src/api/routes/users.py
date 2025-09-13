from fastapi import APIRouter, Depends
from dependencies import (
    get_users_repository,
    get_users_repository
)
from api.controllers.users import UsersController
from domain.users.repository import IUsersRepository

router = APIRouter(prefix="/v1/users", tags=["users"])

def get_controller(repository: IUsersRepository = Depends(get_users_repository)):
    return UsersController(repository)


@router.get("/", summary="List users")
async def index(
    filter_params: str | None, 
    controller: UsersController = Depends(get_controller)
):
    return await controller.index(filter_params)
