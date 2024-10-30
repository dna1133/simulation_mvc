from pydantic_settings import BaseSettings


class EntitySettings(BaseSettings):
    ENTITY_LANDSCAPE: list[str] = [
        "Grass",
        "Rock",
        "Tree",
    ]
    ENTITY_CREATURES: list[str] = [
        "Herbivore",
        "Predator",
    ]
    ENTITY_HEALTH: dict[str, int] = {
        "Grass": 4,
        "Rock": 10,
        "Tree": 10,
        "Herbivore": 12,
        "Predator": 15,
    }
    ENTITY_SPEED: dict[str, int] = {
        "Grass": 0,
        "Rock": 0,
        "Tree": 0,
        "Herbivore": 1,
        "Predator": 2,
    }
    ENTITY_ATTACK_RATE: dict[str, int] = {
        "Grass": 0,
        "Rock": 0,
        "Tree": 0,
        "Herbivore": 2,
        "Predator": 4,
    }
    ENTITY_TARGET: dict[str, str] = {
        "Herbivore": "Grass",
        "Predator": "Herbivore",
    }
    ENTITY_IMG: dict[str, str] = {
        "Predator": "🐯",
        "Herbivore": "🦓",
        "Rock": "🪨",
        "Grass": "🌱",
        "Tree": "🌳",
        "Default": "🟫",
    }
