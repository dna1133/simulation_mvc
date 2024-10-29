from simulation.core.configs.entity import EntitySettings


class Settings(
    EntitySettings,
):
    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
