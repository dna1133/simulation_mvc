from pydantic_settings import SettingsConfigDict
from simulation.core.configs.entity import EntitySettings
from simulation.core.configs.map import MapSettings


class Settings(
    EntitySettings,
    MapSettings,
):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)


settings = Settings()
