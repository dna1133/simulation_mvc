from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum

from simulation.domain.entity.base import Entity
from simulation.domain.entity.landscape import Grass


class Direction(Enum):
    UP = (0, 1)
    DOWN = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


@dataclass
class Creature(Entity, ABC):
    health: int | None = None
    speed: int | None = None
    target_name: str | None = None
    attack_rate: int | None = None
    direction: Direction | None = None

    def move(self):
        step_x, step_y = self.direction.value
        self.x_pos += step_x * self.speed
        self.y_pos += step_y * self.speed

    @abstractmethod
    def attack(self, target: Entity): ...


@dataclass
class Herbivore(Creature):
    def attack(self, target: Grass):
        target.health -= self.attack_rate
        if target.health < 0:
            target.destroy()


@dataclass
class Predator(Creature):
    def attack(self, target: Herbivore):
        target.health -= self.attack_rate
        if target.health < 0:
            target.destroy()
