from fastapi import APIRouter, Depends
from domain.users.repository import IUsersRepository
from domain.users.schema import (
    UserCreate,
    UserListResponse,
    UserResponse
)

def UsersController(
    user_repository = Depends(IUsersRepository)
):
    router = APIRouter(prefix="/v1/users", tags=["users"])
    
    @router.get("/", summary="List Users")
    async def index(filter_params:str | None = None):
        user_data = await user_repository.get_users()
        
        return {
            "success": True,
            "data": user_data
        }

    @router.post("/", summary="Create user")
    async def create(user_param: UserCreate) -> UserResponse:
        user = user_repository.create_user(user=user_param)
        
        return {
            "success": True,
            "data": user
        }

    @router.get("/{user_id}", summary="Get user details")
    async def show(user_id_param: str) -> UserResponse:
        user_data = user_repository.get_user(user_id)

        return {
            "success": True,
            "data": user_data
        }

    return router
