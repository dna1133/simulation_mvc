import pytest

from simulation.app.map_dto import MapDTO
from simulation.domain.entity.creatures import Predator
from simulation.domain.entity.entity_builder import EntityBuilder
from simulation.domain.map.map import Cell, Map


def test_map_to_dto():
    builder = EntityBuilder()
    predator: Predator = builder.add_entity(
        (40, 23),
        name="Predator",
    )
    map_obj = Map()
    map_obj.cells.append(Cell(2, 4))
    map_obj.cells.append(Cell(3, 8))
    map_obj.cells.append(Cell(20, 40, predator))
    map_dto = MapDTO.map_to_dto(map_obj)
    assert isinstance(map_dto, dict)
    assert map_dto[(20, 40)]["name"] == "Predator"
    assert map_dto[(20, 40)]["stats"]["attack_rate"] == 4


def test_dto_to_map():
    dto = {
        (3, 11): None,
        (31, 21): None,
        (12, 42): {
            "name": "Herbivore",
            "position": (12, 42),
            "stats": {
                "x_pos": 30,
                "y_pos": 20,
                "health": 10,
                "attack_rate": 3,
                "speed": 2,
                "direction": (0, 1),
            },
        },
    }
    map_obj = MapDTO.dto_to_map(dto)
    assert isinstance(map_obj, Map)
    x_pos, y_pos = (12, 42)
    for cell in map_obj.cells:
        if cell.x_pos == x_pos and cell.y_pos == y_pos:
            assert cell.contain.name == "Herbivore"
            assert cell.contain.attack_rate == 3
