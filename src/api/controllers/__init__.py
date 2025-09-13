from fastapi import FastAPI

from .devices import DevicesController
from .users import UsersController

class BaseController():
    @staticmethod
    def setup(app: FastAPI) -> None:
        devices_controller = DevicesController()
        users_controller =  UsersController()

        app.include_router(devices_controller)
        app.include_router(users_controller)

        return app
