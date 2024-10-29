from dataclasses import dataclass

from simulation.domain.entity.base import Entity


@dataclass
class Grass(Entity):
    hp: int


@dataclass
class Rock(Entity): ...


@dataclass
class Tree(Entity): ...
