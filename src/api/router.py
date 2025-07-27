from fastapi import FastAPI
from api.controllers import devices, users
from repository.user import UserRepository
from repository.devices import DeviceRepostory

class AppRouter:
    @staticmethod
    def init(app: FastAPI) -> None:
        users_controller = users(user_respository=None)
        devices_controller = devices(device_repository = None)
        
        app.include_router(users)
        app.include_router(devices)

        return app
