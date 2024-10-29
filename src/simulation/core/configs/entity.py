from pydantic_settings import BaseSettings


class EntitySettings(BaseSettings):
    LANDSCAPE: list[str] = [
        "Grass",
        "Rock",
        "Tree",
    ]
    CREATURES: list[str] = [
        "Herbivore",
        "Predator",
    ]
    HEALTH: dict[str, int] = {
        "Grass": 20,
        "Rock": 10,
        "Tree": 10,
        "Herbivore": 10,
        "Predator": 10,
    }
    SPEED: dict[str, int] = {
        "Grass": 0,
        "Rock": 0,
        "Tree": 0,
        "Herbivore": 10,
        "Predator": 15,
    }
    ATTACK_RATE: dict[str, int] = {
        "Grass": 0,
        "Rock": 0,
        "Tree": 0,
        "Herbivore": 0,
        "Predator": 15,
    }
    TARGET: dict[str, str] = {
        "Herbivore": "Grass",
        "Predator": "Herbivore",
    }
