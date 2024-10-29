from abc import ABC, abstractmethod
from dataclasses import dataclass

from simulation.domain.entity.base import Entity


@dataclass
class Creature(Entity, ABC):
    hp: int
    speed: int
    target: str


@dataclass
class Herbivore(Creature): ...


@dataclass
class Predator(Creature): ...
