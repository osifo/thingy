from domain.users.repository import IUsersRepository
from domain.users.schema import User

class UsersRepository(IUsersRepository):
    def get_users(self) -> list[User]:
        return [{
                "id": "1", 
                "name": "test user", 
                "description": "this is a test user"
            }]
