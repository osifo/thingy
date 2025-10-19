from domain.devices.repository import IDevicesRepository
from domain.users.repository import IUsersRepository

from repository.devices import DevicesRepository
from repository.users import UsersRepository


def get_devices_repository() -> IDevicesRepository:
    return DevicesRepository()

def get_users_repository() -> IUsersRepository:
    return UsersRepository()

