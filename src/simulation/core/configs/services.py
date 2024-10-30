from pydantic_settings import BaseSettings


class ServicesSettings(BaseSettings):
    SERVICES_FOV_DEPTH: int = 5
    SERVICES_PATH_RANDOM_STRENTH: int = 50
