from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from functools import lru_cache
from random import randint

from simulation.domain.entity.base import Entity

from simulation.core.configs import settings
from simulation.domain.entity.entity_builder import EntityBuilder


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

    def __str__(self):
        return f"{self.x_pos=}, {self.y_pos=}, {self.contain=}"


@dataclass(kw_only=True)
class BaseMap(ABC):
    cells: list[Cell] = field(default_factory=list)


@lru_cache(1)
@dataclass
class Map(BaseMap):
    _filled_cells = set()
    _entity_cells = dict()

    def create_map(self):
        self._generate_entity_positions()
        for y_pos in range(settings.MAP_HEIGHT):
            for x_pos in range(settings.MAP_WIDTH):
                pos = (x_pos, y_pos)
                if pos in self._entity_cells:
                    self.cells.append(
                        Cell(
                            x_pos,
                            y_pos,
                            EntityBuilder().add_entity(pos, self._entity_cells[pos]),
                        )
                    )
                else:
                    self.cells.append(
                        Cell(
                            x_pos,
                            y_pos,
                        )
                    )

    def _random_position(self):
        return (randint(0, settings.MAP_WIDTH), randint(0, settings.MAP_HEIGHT))

    def _generate_entity_positions(self):
        entity_position = (20, 20)
        for entity_name in settings.ENTITIES_ON_MAP:
            for i in range(settings.ENTITIES_ON_MAP[entity_name]):
                while entity_position in self._filled_cells:
                    entity_position = self._random_position()
                self._filled_cells.add(entity_position)
                self._entity_cells[entity_position] = entity_name

    def __len__(self):
        return len(self.cells)
