from domain.devices.repository import IDevicesRepository
from domain.devices.schema import Device, DeviceCreate

class DevicesRepository(IDevicesRepository):        
    def get_devices(self, filter_params) -> list[Device]:
        return [{
                "id": "1", 
                "name": "test device", 
                "description": "this is a test device"
            }]

    def get_device(self, device: str) -> Device:
        """fetch device details"""
        raise NotImplementedError

    def get_user_devices(self, user_id: str) -> list[Device]:
        """fetch user devices"""
        raise NotImplementedError

    def add_device(self, device_params: DeviceCreate) -> Device:
        """adds a user device"""
        raise NotImplementedError

    def delete_device(self, user_id: str) -> Device:
        """deletes a user device"""
        raise NotImplementedError

def get_devices_repository() -> DevicesRepository:
    return DevicesRepository()
