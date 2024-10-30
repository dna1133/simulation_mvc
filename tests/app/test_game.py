import pytest
from simulation.app.game import Game
from simulation.app.map_dto import MapDTO
from simulation.domain.entity.creatures import Creature, Direction, Herbivore, Predator
from simulation.domain.entity.entity_builder import EntityBuilder
from simulation.domain.map.map import Cell, Map

# from ..conftest import setup_game


def test_move_towards_target():
    game = Game()
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
    game.current_state_from_dto(map_dto)

    for cell in game.map_obj.cells:
        if not cell.is_empty():
            if isinstance(cell.contain, Creature):
                assert cell.contain.name == "Predator"
                old_x_pos, old_y_pos = cell.contain.x_pos, cell.contain.y_pos
                game._entity_move(cell.contain)
                new_x_pos, new_y_pos = cell.contain.x_pos, cell.contain.y_pos
                assert (old_x_pos, old_y_pos) != ((new_x_pos, new_y_pos))


def test_attack_towards_target():
    game = Game()
    builder = EntityBuilder()
    predator: Predator = builder.add_entity(
        (11, 11),
        name="Predator",
    )
    herbivore: Herbivore = builder.add_entity((12, 11), name="Herbivore")
    predator.direction = Direction.RIGHT
    map_obj = Map()
    map_obj.cells.append(Cell(10, 10))
    map_obj.cells.append(Cell(10, 11))
    map_obj.cells.append(Cell(11, 10))
    map_obj.cells.append(Cell(12, 12))
    map_obj.cells.append(Cell(11, 12))
    map_obj.cells.append(Cell(12, 13))
    map_obj.cells.append(Cell(13, 13))
    map_obj.cells.append(Cell(13, 12))
    map_obj.cells.append(Cell(11, 11, predator))
    map_obj.cells.append(Cell(12, 11, herbivore))
    map_dto = MapDTO.map_to_dto(map_obj)
    game.current_state_from_dto(map_dto)
    old_health = game.map_obj.cells[-1].contain.health
    attack_success = game._entity_attack(predator)
    new_health = game.map_obj.cells[-1].contain.health
    assert game._scan_target(predator, fov_depth=2) == game.map_obj.cells[-1]
    assert attack_success
    assert new_health != old_health
