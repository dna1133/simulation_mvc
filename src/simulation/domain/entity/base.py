from abc import ABC
from dataclasses import dataclass


@dataclass
class Entity(ABC):
    x_pos: int
    y_pos: int
    img: str

    @property
    def name(self) -> str:
        return self.__class__.__name__

    def destroy(self) -> None:
        self.x_pos = None
        self.y_pos = None
