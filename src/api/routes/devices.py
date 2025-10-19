from fastapi import APIRouter, Depends
from api.controllers.devices import (
    DevicesController,
    get_devices_controller
)
from domain.devices.repository import IDevicesRepository
from repository.devices import get_devices_repository

router = APIRouter(prefix="/v1/devices", tags=["devices"])

@router.get("/", summary="List devices")
async def index(
    filter_params: str | None = None, 
    controller: DevicesController = Depends(get_devices_controller)
):
    return await controller.index(filter_params)
