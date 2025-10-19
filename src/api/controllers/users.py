from fastapi import APIRouter, Depends
from domain.users.repository import IUsersRepository
from repository.users import get_users_repository
from domain.users.schema import (
    UserCreate,
    UserListResponse,
    UserResponse
)

class UsersController():
    def __init__(self, repository: IUsersRepository = Depends(get_users_repository)):
        self.repo = repository
    
    async def index(self, filter_params: str | None = None):
        user_data = await self.repo.get_users(filter_params)
        return {
            "success": True,
            "data": user_data
        }

    async def create(self, user_param: UserCreate) -> UserResponse:
        user_data = self.repo.create_user(user=user_param)
            
        return {
            "success": True,
            "data": user_data
        }


    async def show(user_id_param: str) -> UserResponse:
        user_data = user_repository.get_user(user_id)

        return {
            "success": True,
            "data": user_data
        }

def get_users_controller(repository: IUsersRepository = Depends(get_users_repository)) -> UsersController:
    return UsersController(repository)
