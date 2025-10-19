from core import BaseConfig
from enum import Enum
from dotenv import load_dotenv

load_dotenv()
class Environment(Enum):
    TEST = 'test'
    DEV = 'dev'
    STAGING = 'staging'
    PROD = 'production'

class AppConfig(BaseConfig):
    APP_ENV = BaseConfig.get_env('APP_ENV')
    APP_NAME = 'Things by Outside Labs'
    API_VERSION =  BaseConfig.get_env('API_VERSION')
    
    @property
    def is_dev(self) -> bool:
        return self.APP_ENV == Environment.DEV.value
    
    @property
    def is_test(self) -> bool:
        return self.APP_ENV.lower() == Environment.TEST.value.lower()
    