from uuid import uuid4
from datetime import datetime, timezone
from domain.base import BaseModel

from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime
)

class User(BaseModel):
    __tablename__ = "users"

    def __init__(self, **kwargs):
        if 'id' not in kwargs:
            kwargs['id'] =  str(uuid4())
        super().__init__(**kwargs)

    id = Column(String(40), primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    firstname = Column(String(255))
    lastname = Column(String(255))
    age = Column(Integer)
    created_at = Column(
        DateTime(timezone=True), 
        index=True, 
        nullable=False, 
        default=datetime.now(timezone.utc)
    )
    updated_at = Column(
        DateTime(timezone=True), 
        index=True,
        onupdate = lambda: datetime.now(timezone.utc)
    )
