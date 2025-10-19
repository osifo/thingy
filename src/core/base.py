import os
from typing import Callable, TypeVar

T = TypeVar('T') #for generics typechecking

class BaseConfig:
    @staticmethod
    def get_env(
        key: str, 
        is_required: bool = True, 
        defaut="", 
        expectd_type: Callable[[str], T] = str
    ) -> T:
        value = os.getenv(key) or ""

        if value is None and is_required:
            raise ValueError("Required environment variale {key} is not set")

        if value is not None and expectd_type is not str:
            try:
                expectd_type(value)
            except ValueError:
                raise ValueError("Value for env variable {key} has an invalid type. Expected {expected_type.__name__}")
        try:
            return expectd_type(value)
        except:
            raise ValueError(f"Environment variable '{key}' value '{value}' cannot be cast to {expectd_type.__name__}")
    
    