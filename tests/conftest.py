import pytest

from simulation.app.game import Game
from simulation.app.map_dto import MapDTO
from simulation.domain.map.map import Map


# @pytest.fixture
# def setup_game():
#     # Создаем экземпляр карты и игры
#     game = Game
#     map_obj = Map()
#     width = 10
#     height = 10
#     entities_on_map = {
#         "Grass": 2,
#         "Rock": 2,
#         "Tree": 1,
#         "Herbivore": 1,
#         "Predator": 1,
#     }
#     map_obj._generate_entity_positions(
#         start_position=(2, 2),
#         entities_on_map=entities_on_map,
#         width=width,
#         height=height,
#     )
#     map_dto = MapDTO.map_to_dto(map_obj)
#     game.current_state_from_dto(game, map_dto)
#     return game


# def test_move_towards_target(setup_game):
#     game, creature = setup_game

#     # Запускаем функцию _move() и проверяем, переместилось ли существо к цели
#     result = game._move(creature)

#     # Проверяем, что результат True, что означает, что цель найдена и движение произошло
#     assert result is True
#     assert creature.direction == Direction.UP  # Направление изменено на цель
#     PathFinder.find_direction.assert_called_once()  # Проверка вызова метода поиска направления


# def test_move_without_target(setup_game):
#     game, creature = setup_game
#     game.map_obj.cells[3][3].contain = None  # Убираем цель

#     # Запускаем функцию _move() и проверяем, что движение происходит в другом направлении
#     result = game._move(creature)

#     # Проверяем, что результат False, так как цель не найдена
#     assert result is False
#     assert (
#         creature.direction == Direction.LEFT
#     )  # Существо выбрало альтернативное направление
#     PathFinder.choose_direction.assert_called_once()  # Проверка вызова метода выбора направления


# def test_collision_with_obstacle(setup_game):
#     game, creature = setup_game
#     obstacle_cell = Cell(
#         x_pos=3, y_pos=2, contain=Rock(x_pos=3, y_pos=2)
#     )  # Препятствие на пути
#     game.map_obj.cells[3][2] = obstacle_cell

#     # Запускаем функцию _move() и проверяем, что столкновение обработано корректно
#     result = game._move(creature)

#     # Проверка, что существо осталось на месте из-за препятствия
#     assert result is True
#     assert (creature.x_pos, creature.y_pos) == (2, 2)
#     PathFinder.choose_direction.assert_called_with(2, 2, strength=1000)
