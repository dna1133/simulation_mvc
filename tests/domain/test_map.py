import pytest

from simulation.domain.entity.creatures import Predator
from simulation.domain.map.map import Cell, Map


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
    c = Cell(x_pos=1, y_pos=11, contain=predator)
    created_map = Map()
    created_map.cells.append(c)
    created_map.cells.append(c)
    assert created_map.cells == [c, c]
