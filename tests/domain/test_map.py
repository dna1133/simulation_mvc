import pytest

from simulation.domain.entity.creatures import Predator
from simulation.domain.map.map import Cell, Map

from simulation.core.configs import settings


@pytest.fixture
def mock_creature_stats():
    return {
        "x_pos": 20,
        "y_pos": 20,
        "health": 10,
        "speed": 3,
        "attack_rate": 2,
    }


def test_cell_create_success(mock_creature_stats):
    predator = Predator(**mock_creature_stats)
    cell = Cell(x_pos=1, y_pos=11, contain=predator)
    assert cell.contain == predator
    assert cell.contain.health == 10
    assert cell.is_empty() == False


def test_map_create(mock_creature_stats):
    predator = Predator(**mock_creature_stats)
    map = Map()
    map.create_map()
    assert isinstance(map._filled_cells, set)
    assert isinstance(map.cells, list)
    assert len(map) == (settings.MAP_HEIGHT * settings.MAP_WIDTH)
    for i in range(len(map)):
        if isinstance(map.cells[i].contain, Predator):
            assert map.cells[i].contain.name == "Predator"
            assert map.cells[i].contain.attack_rate == 4
