from pydantic_settings import BaseSettings


class MapSettings(BaseSettings):
    MAP_WIDTH: int
    MAP_HEIGHT: int
    ENTITIES_ON_MAP: dict[str, int] = {
        "Grass": 20,
        "Rock": 10,
        "Tree": 10,
        "Herbivore": 10,
        "Predator": 10,
    }
