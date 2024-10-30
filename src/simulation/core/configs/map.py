from pydantic_settings import BaseSettings


class MapSettings(BaseSettings):
    MAP_WIDTH: int = 21
    MAP_HEIGHT: int = 21
    ENTITIES_ON_MAP: dict[str, int] = {
        "Grass": 10,
        "Rock": 5,
        "Tree": 5,
        "Herbivore": 5,
        "Predator": 3,
    }
