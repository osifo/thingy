import traceback;
from fastapi import APIRouter, status, Depends
from domain.devices.repository import IDevicesRepository
from domain.devices.schema import (
    DeviceResponse,
    DeviceListResponse,
    DeviceCreate
)

def DevicesController(device_repository=Depends(IDevicesRepository)):
    router = APIRouter(prefix="/v1/devices", tags=["devices"])

    @router.get("/", summary="List devices")
    async def index(filter_params: str | None = None) -> DeviceListResponse:
        device_list =  device_repository.get_devices(filter_params)
        return {
            "success": True,
            data: device_list
        }
    
    @router.post("/", summary="Add a device")
    async def create(device_param: DeviceCreate) -> DeviceResponse:
        new_device = device_repository.add_device(device_param)
        return {
            "success": True,
            "data": new_device
        }

    
    @router.get("/{device_id}", summary="Get device details")
    async def show(device_id: str) -> DeviceResponse:
        device = device_repository.get_device(device_id)
        return {
            "success": True,
            "data": device
        }

    return router