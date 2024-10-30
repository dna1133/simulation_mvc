from abc import ABC
from dataclasses import dataclass, field

from simulation.core.configs import settings


@dataclass
class Entity(ABC):
    x_pos: int
    y_pos: int
    destroyed: bool = False
    _img: str | None = None

    @property
    def name(self) -> str:
        return self.__class__.__name__

    @property
    def img(self) -> str:
        if not self._img:
            return settings.ENTITY_IMG[self.name]
        return self._img

    @img.setter
    def img(self, image) -> None:
        self._img = image

    def destroy(self) -> None:
        self.destroyed = True

    def __str__(self):
        return self.name
