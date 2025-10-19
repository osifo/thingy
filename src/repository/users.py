from fastapi import Depends
from sqlalchemy.orm import Session
from domain.users.repository import IUsersRepository
from domain.users.schema import User, User, UserCreate
from domain.users.model import User as UserModel
from core.database import get_database
from sqlalchemy.exc import IntegrityError

class UsersRepository(IUsersRepository):
    def __init__(self, database: Session):
        self.db = database

    async def get_users(self, filter_params: str | None = None) -> list[User]:
        users = self.db.query(UserModel).order_by(UserModel.created_at.desc()).all()
        return [User.model_validate(user_record) for user_record in users]
    
    async def get_user(self, user_id: str) -> User:
        user_data = self.db.query(UserModel).get({ "id": user_id })

        if not user_data:
            raise Exception(f"User not found with id {user_id}")
        return User.model_validate(user_data)
    
    async def create_user(self, user_param: UserCreate) -> User:
        try:
            new_user = UserModel(
                **user_param.model_dump()
            )

            if not new_user:
                raise Exception("Invalid user")
            
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
            return User.model_validate(new_user)
        except IntegrityError as error:
            self.db.rollback()
            raise Exception(f"Another user already exists with these details {str(error)}")
    
    async def delete_user(self, user_id: str) -> User:
        user = self.db.query(UserModel).get({ id: user_id })

        if not user:
            raise Exception(f"User not found with id: {user_id}")
        return User.model_validate(user)

def get_users_repository(database: Session = Depends(get_database)) -> IUsersRepository:
    return UsersRepository(database)

