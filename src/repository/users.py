from domain.users.repository import IUsersRepository
from domain.users.schema import User, User, UserCreate

class UsersRepository(IUsersRepository):
    async def get_users(self, filter_params: str) -> list[User]:
        return [{
                "id": "1", 
                "name": "test user", 
                "description": "this is a test user"
            }]
    
    def get_user(self, user_id: str) -> list[User]:
        """fetch users"""
        raise NotImplementedError
    
    def create_user(self, user_param: UserCreate) -> User:
        """adds a user device"""
        raise NotImplementedError
    
    def delete_user(self, user_id: str) -> User:
        """deletes a user device"""
        raise NotImplementedError

