from fastapi import FastAPI

from .devices import router as devices_router
from .users import router as users_router
from repository.devices import DevicesRepository
from repository.users import UsersRepository

class AppRouter():
    @staticmethod
    def setup(app: FastAPI) -> None:
        app.include_router(devices_router)
        app.include_router(users_router)

        return app
