from pydantic_settings import SettingsConfigDict
from simulation.core.configs.common import CommonSettings
from simulation.core.configs.entity import EntitySettings
from simulation.core.configs.map import MapSettings
from simulation.core.configs.services import ServicesSettings


class Settings(
    EntitySettings,
    MapSettings,
    ServicesSettings,
    CommonSettings,
):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)


settings = Settings()
