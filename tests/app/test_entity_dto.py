from simulation.domain.entity.creatures import Direction, Herbivore
from simulation.domain.entity.landscape import Rock
from simulation.app.entity_dto import EntityDTO


def test_herbivore_to_dto_success():
    herbivore = Herbivore(
        x_pos=1,
        y_pos=2,
        health=10,
        target_name="Grass",
        attack_rate=5,
        speed=3,
        direction=Direction.DOWN,
    )
    herbivore_dto = EntityDTO.entity_to_dto(herbivore)
    assert herbivore_dto["name"] == herbivore.name
    assert herbivore_dto["stats"]["speed"] == 3
    assert herbivore_dto["stats"]["direction"] == (0, -1)


def test_herbivore_from_dto_success():
    dto = {
        "name": "Herbivore",
        "position": (30, 20),
        "stats": {
            "x_pos": 30,
            "y_pos": 20,
            "health": 10,
            "attack_rate": 3,
            "speed": 2,
            "direction": (0, 1),
        },
    }
    herbivore = EntityDTO.dto_to_entity(dto)
    assert isinstance(herbivore, Herbivore)
    assert herbivore.direction == Direction.UP


def test_rock_from_dto_success():
    dto = {
        "name": "Rock",
        "position": (30, 20),
        "stats": {
            "x_pos": 30,
            "y_pos": 20,
        },
    }
    rock = EntityDTO.dto_to_entity(dto)
    assert isinstance(rock, Rock)
