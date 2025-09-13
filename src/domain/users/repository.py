from abc import ABC, abstractmethod
from .schema import User, UserCreate

class IUsersRepository(ABC):
    @abstractmethod
    async def get_users(filter_params: str | None = None) -> list[User]:
        """fetch users"""
        raise NotImplementedError

    @abstractmethod
    async def get_user(self, user_id: str) -> list[User]:
        """fetch users"""
        raise NotImplementedError
    
    @abstractmethod
    def create_user(self, user_param: UserCreate) -> User:
        """adds a user device"""
        raise NotImplementedError
    
    @abstractmethod
    def delete_user(self, user_id: str) -> User:
        """deletes a user device"""
        raise NotImplementedError
