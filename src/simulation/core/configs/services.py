from pydantic_settings import BaseSettings


class ServicesSettings(BaseSettings):
    SERVICES_FOV_DEPTH: int = 3
    SERVICES_PATH_RANDOM_STRENTH: int = 50
