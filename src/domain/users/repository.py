from abc import ABC, abstractmethod
from .schema import User, UserCreate

class IUsersRepository(ABC):
    @abstractmethod
    def get_users(self) -> list[User]:
        """fetch users"""
        raise NotImplementedError

    def get_user(self, user_id: str) -> list[User]:
        """fetch users"""
        raise NotImplementedError
    
    def create_user(self, user_param: UserCreate) -> User:
        """adds a user device"""
        raise NotImplementedError

    def delete_user(self, user_id: str) -> User:
        """deletes a user device"""
        raise NotImplementedError
