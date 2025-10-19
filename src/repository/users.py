from fastapi import Depends
from sqlalchemy.orm import Session
from domain.users.repository import IUsersRepository
from domain.users.schema import User, User, UserCreate
from domain.users.model import User as UserModel
from core.database import get_database

class UsersRepository(IUsersRepository):
    def __init__(self, database: Session):
        self.db = database

    async def get_users(self, filter_params: str | None = None) -> list[User]:
        users = self.db.query(UserModel).order_by(UserModel.created_at.desc()).all()
        return [User.from_orm(user_record) for user_record in users]
    
    async def get_user(self, user_id: str) -> User:
        """fetch users"""
        raise NotImplementedError
    
    async def create_user(self, user_param: UserCreate) -> User:
        """adds a user device"""
        raise NotImplementedError
    
    async def delete_user(self, user_id: str) -> User:
        """deletes a user device"""
        raise NotImplementedError

def get_users_repository(database: Session = Depends(get_database)) -> IUsersRepository:
    return UsersRepository(database)

