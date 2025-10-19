from abc import ABC, abstractmethod
from domain.users.schema import User, UserCreate

class IUsersRepository(ABC):
    @abstractmethod
    async def get_users(self, filter_params: str | None = None) -> list[User]:
        """fetch users"""
        raise NotImplementedError

    @abstractmethod
    async def get_user(self, user_id: str) -> User:
        """fetch users"""
        raise NotImplementedError
    
    @abstractmethod
    async def create_user(self, user_param: UserCreate) -> User:
        """adds a user device"""
        raise NotImplementedError
    
    @abstractmethod
    async def delete_user(self, user_id: str) -> User:
        """deletes a user device"""
        raise NotImplementedError
