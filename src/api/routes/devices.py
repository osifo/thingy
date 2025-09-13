from fastapi import APIRouter, Depends
from dependencies import (
    get_devices_repository,
    get_users_repository
)
from api.controllers.devices import DevicesController
from domain.devices.repository import IDevicesRepository

router = APIRouter(prefix="/v1/devices", tags=["devices"])

def get_controller(repository: IDevicesRepository = Depends(get_devices_repository)):
    return DevicesController(repository)


@router.get("/", summary="List devices")
async def index(
    filter_params: str | None = None, 
    controller: DevicesController = Depends(get_controller)
):
    return await controller.index(filter_params)
