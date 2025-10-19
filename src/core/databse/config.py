from dataclasses import dataclass
from functools import cached_property
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from core import BaseConfig


@dataclass(frozen=True)
class Database(BaseConfig):
    @cached_property
    def DATABASE_URL(self) -> str | URL:
        username = self.get_env('DB_USERNAME')
        password = self.get_env('DB_PASSWORD')
        db_name = self.get_env('DB_NAME')
        db_host = self.get_env('DB_HOST')
        db_port: int = self.get_env('DB_PORT', expectd_type=int)

        return URL.create(
            "mysql+pymysql",
            username,
            password,
            host=db_host,
            port=db_port,
            database=db_name
        )
    
    @cached_property
    def SessionLocal(self):
        database_engine = create_engine(self.DATABASE_URL)
        return sessionmaker(autocommit=False, autoflush=True, bind=database_engine)

    
@dataclass(frozen=True)
class TestDatabase(Database):
    
    @cached_property
    def DATABASE_URL(self) -> str:
        return 'sqlite:///./things_test_database.db'
    
    @cached_property
    def SessionLocal(self):
        connect_args = {"check_same_thread": False}
        database_engine = create_engine(self.DATABASE_URL, connect_args=connect_args)
        return sessionmaker(autocommit=False, autoflush=True, bind=database_engine)




