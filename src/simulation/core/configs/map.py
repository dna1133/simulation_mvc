from pydantic_settings import BaseSettings


class MapSettings(BaseSettings):
    MAP_WIDTH: int = 41
    MAP_HEIGHT: int = 41
    ENTITIES_ON_MAP: dict[str, int] = {
        "Grass": 20,
        "Rock": 10,
        "Tree": 10,
        "Herbivore": 15,
        "Predator": 10,
    }
