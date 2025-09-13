from abc import ABC, abstractmethod;
from .schema import Device, DeviceCreate

class IDevicesRepository(ABC):
    @abstractmethod
    def get_devices(self) -> list[Device]:
        """fetch devices"""
        raise NotImplementedError

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
