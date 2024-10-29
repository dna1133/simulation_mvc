import pytest

from simulation.domain.entity.creatures import Direction, Herbivore, Predator
from simulation.domain.entity.landscape import Grass, Rock, Tree


def test_rock_create_success():
    rock = Rock(x_pos=1, y_pos=2)
    assert rock.x_pos == 1
    assert rock.y_pos == 2
    assert rock.name == "Rock"


def test_tree_create_success():
    tree = Tree(x_pos=1, y_pos=2)
    assert tree.x_pos == 1
    assert tree.y_pos == 2
    assert tree.name == "Tree"


def test_grass_create_success():
    grass = Grass(x_pos=1, y_pos=2, health=10)
    assert grass.x_pos == 1
    assert grass.y_pos == 2
    assert grass.health == 10
    assert grass.name == "Grass"
    assert isinstance(grass.img, str)


def test_herbivore_create_success():
    herbivore = Herbivore(
        x_pos=1,
        y_pos=2,
        health=10,
        target_name="Grass",
        attack_rate=5,
        speed=3,
        direction=Direction.DOWN,
    )
    assert herbivore.target_name == "Grass"
    assert herbivore.speed == 3
    assert herbivore.direction.value == (0, -1)


def test_predator_create_success():
    predator = Predator(
        x_pos=20,
        y_pos=20,
        health=10,
        speed=2,
        attack_rate=5,
        direction=Direction.DOWN,
    )
    assert predator.y_pos == 20
    predator.move()
    assert predator.attack_rate == 5
    assert predator.name == "Predator"
    assert predator.direction.value == (0, -1)
    assert predator.y_pos == 18


def test_entity_fail():
    with pytest.raises(TypeError):
        herbivore = Herbivore()


def test_creature_attack():
    predator = Predator(
        x_pos=20,
        y_pos=20,
        health=10,
        speed=2,
        attack_rate=5,
        direction=Direction.DOWN,
    )
    herbivore = Herbivore(
        x_pos=1,
        y_pos=2,
        health=10,
        attack_rate=5,
        speed=3,
        direction=Direction.DOWN,
    )
    predator.attack(herbivore)
    assert herbivore.health == 5
