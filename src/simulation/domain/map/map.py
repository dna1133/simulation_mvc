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
    _contain: Entity | None = None

    @abstractmethod
    def is_empty(self) -> bool: ...


@dataclass
class Cell(BaseCell):
    @property
    def contain(self) -> Entity:
        return self._contain

    @contain.setter
    def contain(self, entity: Entity | None) -> None:
        self._contain = entity

    def is_empty(self) -> bool:
        if self.contain:
            return False
        return True

    def __str__(self):
        return f"{self.x_pos=}, {self.y_pos=}, {self.contain=}"


# @lru_cache(1)
@dataclass
class Map:
    cells: list[Cell] = field(default_factory=list)
    _filled_cells = set()
    _entity_cells = dict()

    def create_map(
        self, width: int = settings.MAP_WIDTH, height: int = settings.MAP_HEIGHT
    ):
        if not self._filled_cells:
            self._generate_entity_positions()
        for y_pos in range(height):
            for x_pos in range(width):
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

    def _random_position(
        self, width: int = settings.MAP_WIDTH, height: int = settings.MAP_HEIGHT
    ):
        return (randint(0, width), randint(0, height))

    def _generate_entity_positions(
        self,
        start_position: tuple = (20, 20),
        entities_on_map: dict = settings.ENTITIES_ON_MAP,
        width: int = settings.MAP_WIDTH,
        height: int = settings.MAP_HEIGHT,
    ):
        entity_position = start_position
        for entity_name in entities_on_map:
            for i in range(entities_on_map[entity_name]):
                while entity_position in self._filled_cells:
                    entity_position = self._random_position(width, height)
                self._filled_cells.add(entity_position)
                self._entity_cells[entity_position] = entity_name

    def __len__(self):
        return len(self.cells)

    def cell_from_position(self, position: tuple[int, int]) -> Cell:
        for cell in self.cells:
            if (cell.x_pos, cell.y_pos) == position:
                return cell
