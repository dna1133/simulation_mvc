import time

from dataclasses import dataclass

from simulation.app.map_dto import MapDTO
from simulation.core.configs import settings
from simulation.domain.entity.creatures import Creature
from simulation.domain.map.map import Map
from simulation.services.path_finder import PathFinder


class Game:
    def __init__(self):
        self.turn: int = 1
        self.paused: bool = True
        self.map_obj: Map

    def start_game(self, map_dto: dict | None = None) -> None:
        if map_dto:
            self.current_state_from_dto(map_dto)
        else:
            self.map_obj = Map()
            self.map_obj.create_map()

    def current_state_to_dto(self, map_obj: Map) -> dict:
        return MapDTO.map_to_dto(map_obj)

    def current_state_from_dto(self, dto: dict) -> Map:
        self.map_obj = MapDTO.dto_to_map(dto)

    def next_turn(self):
        for cell in self.map_obj.cells:
            if not cell.is_empty():
                if isinstance(cell.contain, Creature):
                    if not self._attack(cell.contain):
                        self._move(cell.contain)

    def _move(self, entity: Creature) -> bool:
        entity_fov = PathFinder.entity_fov(entity.x_pos, entity.y_pos, entity.direction)
        for cell_pos in entity_fov:
            for cell in self.map_obj.cells:
                if not cell.is_empty():
                    if (
                        cell.x_pos,
                        cell.y_pos,
                    ) == cell_pos and entity.target_name == cell.contain.name:
                        entity.direction = PathFinder.find_direction(
                            (cell.x_pos, cell.y_pos), entity.direction.value
                        )
                        print(f"Target found = {cell.contain.name}")
                        return True
        entity.direction = PathFinder.choose_direction(
            entity.x_pos, entity.y_pos, entity.direction
        )
        current_pos_x, current_pos_y = entity.x_pos, entity.y_pos
        entity.move()
        new_pos_x, new_pos_y = entity.x_pos, entity.y_pos
        for cell in self.map_obj.cells:
            if (cell.x_pos, cell.y_pos) == (current_pos_x, current_pos_y):
                temp_cell = cell
            if (cell.x_pos, cell.y_pos) == (new_pos_x, new_pos_y):
                if not cell.is_empty():
                    entity.x_pos, entity.y_pos = current_pos_x, current_pos_y
                    entity.direction = PathFinder.choose_direction(
                        entity.x_pos, entity.y_pos, strength=1000
                    )
                    return True
                else:
                    temp_cell.contain = None
                    cell.contain = entity

    def _attack(self, entity: Creature) -> bool: ...

    def pause_simulation(self) -> None:
        self.paused = True

    def game_loop(self) -> None:
        while not self.paused:
            time.sleep()
            self.next_turn()
