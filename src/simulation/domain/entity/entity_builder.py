from dataclasses import dataclass
from random import choice
from simulation.domain.entity.base import Entity
from simulation.domain.entity.creatures import Direction, Herbivore, Predator
from simulation.domain.entity.landscape import Grass, Rock, Tree

from simulation.core.configs import settings
from simulation.domain.exception import ApplicationException

_entity_dict = {
    "Grass": Grass,
    "Rock": Rock,
    "Tree": Tree,
    "Herbivore": Herbivore,
    "Predator": Predator,
}


@dataclass
class EntityBuilder:
    def add_entity(position: tuple, name: str) -> Entity:
        x_pos, y_pos = position
        if name == "Tree" or "Rock":
            return _entity_dict[name](x_pos=x_pos, y_pos=y_pos)
        elif name == "Grass":
            return _entity_dict[name](
                x_pos=x_pos, y_pos=y_pos, health=settings.ENTITY_HEALTH[name]
            )
        elif name == "Herbivore" or "Predator":
            return _entity_dict[name](
                x_pos=x_pos,
                y_pos=y_pos,
                health=settings.ENTITY_HEALTH[name],
                speed=settings.ENTITY_SPEED[name],
                target_name=settings.ENTITY_TARGET[name],
                attack_rate=settings.ENTITY_ATTACK_RATE[name],
                direction=choice(list(Direction)),
            )
        else:
            raise ApplicationException()
