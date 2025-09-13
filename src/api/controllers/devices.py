import traceback;
from fastapi import APIRouter, status
from domain.devices.repository import IDevicesRepository
from domain.devices.schema import (
    DeviceResponse,
    DeviceListResponse,
    DeviceCreate
)
# from dependencies import get_device_repository

class DevicesController:
    def __init__ (self, repo: IDevicesRepository):
        self.repo = repo
    
    async def index(self, filter_params: str | None = None):
        device_list =  self.repo.get_devices(filter_params)
        return {
            "success": True,
            "data": device_list
        }
    
    async def create(self, device_param: DeviceCreate) -> DeviceResponse:
        new_device = self.repo.add_device(device_param)
        return {
            "success": True,
            "data": new_device
        }

    async def show(self, device_id: str) -> DeviceResponse:
        device = self.repo.get_device(device_id)
        return {
            "success": True,
            "data": device
        }
