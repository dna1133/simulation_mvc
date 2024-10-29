from dataclasses import dataclass

from simulation.domain.entity.base import Entity


@dataclass
class Grass(Entity):
    health: int | None = None


@dataclass
class Rock(Entity): ...


@dataclass
class Tree(Entity): ...
