import pytest

from simulation.app.game import Game
from simulation.domain.map.map import Map


@pytest.fixture
def setup_game():
    # Создаем экземпляр карты и игры
    game = Game
    map_obj = Map()
    width = 10
    height = 10
    entities_on_map = {
        "Grass": 2,
        "Rock": 2,
        "Tree": 1,
        "Herbivore": 1,
        "Predator": 1,
    }
    map_obj._generate_entity_positions(
        start_position=(2, 2),
        entities_on_map=entities_on_map,
        width=width,
        height=height,
    )
    # game.map_obj.
