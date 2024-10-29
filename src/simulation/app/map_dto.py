from simulation.app.entity_dto import EntityDTO
from simulation.domain.map.map import Cell, Map


class MapDTO:
    @staticmethod
    def map_to_dto(map: Map) -> dict:
        map_dto = {}
        for cell in map.cells:
            if cell.is_empty():
                map_dto[(cell.x_pos, cell.y_pos)] = None
            else:
                map_dto[(cell.x_pos, cell.y_pos)] = EntityDTO.entity_to_dto(
                    cell.contain
                )
        return map_dto

    @staticmethod
    def dto_to_map(dto: dict) -> Map:
        map_obj = Map()
        for key, value in dto.items():
            x_pos, y_pos = key
            if value:
                map_obj.cells.append(Cell(x_pos, y_pos, EntityDTO.dto_to_entity(value)))
            else:
                map_obj.cells.append(Cell(x_pos, y_pos))
        return map_obj
