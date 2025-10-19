from typing import Iterator
from sqlalchemy.orm import Session
from core.app import AppConfig
from core.databse.config import TestDatabase, Database

DATABASE_CONFIG = TestDatabase() if AppConfig.is_test else Database()

def get_database() -> Iterator[Session]:
    db = DATABASE_CONFIG.SessionLocal()

    try:
        yield db
        db.commit()
    except Exception as error:
        db.rollback()
        raise error
    finally:
        db.close()

