from simulation.domain.entity.base import Entity
from simulation.domain.entity.creatures import Direction, Herbivore, Predator
from simulation.domain.entity.landscape import Grass, Rock, Tree
from simulation.domain.exception import ApplicationException


_entity_dict = {
    "Grass": Grass,
    "Rock": Rock,
    "Tree": Tree,
    "Herbivore": Herbivore,
    "Predator": Predator,
}


class EntityDTO:

    @staticmethod
    def entity_to_dto(entity: Entity) -> dict:
        stats = {
            "name": entity.name,
            "position": (entity.x_pos, entity.y_pos),
            "stats": {
                "x_pos": entity.x_pos,
                "y_pos": entity.y_pos,
            },
        }
        if entity.name == "Grass":
            stats["stats"]["health"] = entity.health
        elif entity.name == "Herbivore" or entity.name == "Predator":
            stats["stats"]["health"] = entity.health
            stats["stats"]["speed"] = entity.speed
            stats["stats"]["target_name"] = entity.target_name
            stats["stats"]["attack_rate"] = entity.attack_rate
            stats["stats"]["direction"] = entity.direction.value
        return stats

    @staticmethod
    def dto_to_entity(dto: dict, entity_dict=_entity_dict) -> Entity:
        entity = entity_dict[dto["name"]](**dto["stats"])
        if entity.name == "Herbivore" or entity.name == "Predator":
            entity.direction = Direction(dto["stats"]["direction"])
        return entity
