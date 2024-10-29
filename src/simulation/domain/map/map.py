from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from functools import lru_cache

from simulation.domain.entity.base import Entity

from simulation.core.configs import settings


@dataclass
class BaseCell(ABC):
    x_pos: int
    y_pos: int
    contain: Entity | None = None

    @abstractmethod
    def is_empty(self) -> bool: ...


@dataclass
class Cell(BaseCell):
    def is_empty(self) -> bool:
        if self.contain:
            return False
        return True


@dataclass(kw_only=True)
class BaseMap(ABC):
    cells: list[Cell] = field(default_factory=list)


@lru_cache(1)
@dataclass
class Map(BaseMap):
    def create_map(self):
        for y in settings.MAP_HEIGHT:
            for x in settings.MAP_WIDTH:
                ...
