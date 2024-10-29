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
    hp: int
    speed: int
    target: str
    attack_rate: int
    direction: Direction

    @abstractmethod
    def move(self):
        step_x, step_y = self.direction * self.speed
        self.x_pos += step_x
        self.y_pos += step_y

    @abstractmethod
    def attack(self, target: Grass):
        target.hp -= self.attack_rate
        if target.hp < 0:
            target.destroy()


@dataclass
class Herbivore(Creature):
    def attack(self, target: Grass): ...


@dataclass
class Predator(Creature):
    def attack(self, target: Herbivore): ...
