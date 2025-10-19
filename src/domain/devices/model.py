from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    Boolean,
    UniqueConstraint,
    ForeignKey
)

from domain.base import BaseModel

class Device(BaseModel):
    __tablename__ = "devices"

    def __init__(self, **kwargs):
        if 'id' not in kwargs:
            kwargs['id'] = uuid4()
        super().__init__(**kwargs)

    id = Column(String(40), primary_key=True, index=True)
    name = Column(String(255), index=True, nullable=True)
    description = Column(String(255))
    is_active = Column(Boolean)
    user_id = Column(String(40), ForeignKey("users.id"))
    created_at = Column(
        DateTime(timezone=True), 
        index=True, 
        nullable=False, 
        default = datetime.now(timezone.utc),
    )
    updated_at = Column(
        DateTime(timezone=True),
        onupdate = lambda: datetime.now(timezone.utc)
    )

    __table_args__ = (
        UniqueConstraint('name', 'user_id', name='unique_user_device_name'),
    )
