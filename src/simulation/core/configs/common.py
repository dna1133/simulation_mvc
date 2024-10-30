from pydantic_settings import BaseSettings


class CommonSettings(BaseSettings):
    TIME_TO_TICK: int = 1
