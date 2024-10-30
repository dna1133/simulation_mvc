from dataclasses import dataclass
import random

from simulation.core.configs import settings
from simulation.domain.entity.creatures import Direction


@dataclass
class PathFinder:
    @staticmethod
    def entity_fov(
        x_position: int,
        y_position: int,
        direction: Direction,
        fov_depth: int = settings.SERVICES_FOV_DEPTH,
        max_x: int = settings.MAP_WIDTH,
        max_y: int = settings.MAP_HEIGHT,
    ) -> list[tuple[int, int]]:
        cells_in_view = []
        dx, dy = direction.value

        # Проходим по каждому уровню глубины, начиная от 1 до fov_depth
        for depth in range(1, fov_depth + 1):
            # Текущая позиция на глубине поиска
            try:
                base_x = x_position + dx * depth
            except TypeError:
                base_x = dx * depth
            # print(type(x_position), x_position)
            # if x_position != None:
            #     base_x = x_position + dx * depth
            # else:
            #     base_x = dx * depth
            if y_position != None:
                base_y = y_position + dy * depth
            else:
                base_y = dy * depth

            # В зависимости от глубины определяем "ширину" конуса
            for offset in range(-depth, depth + 1):
                # Проверяем клетки по горизонтальному или вертикальному направлению
                if abs(dx) > abs(dy):
                    x = base_x
                    y = base_y + offset
                else:
                    x = base_x + offset
                    y = base_y

                # Проверяем, что клетки находятся в пределах карты
                if 0 <= x < max_x and 0 <= y < max_y:
                    cells_in_view.append((x, y))

        return cells_in_view

    @staticmethod
    def choose_direction(
        x_position: int,
        y_position: int,
        direction: Direction,
        max_x: int = settings.MAP_WIDTH,
        max_y: int = settings.MAP_HEIGHT,
        strength: int = settings.SERVICES_PATH_RANDOM_STRENTH,
    ) -> Direction:
        dx, dy = direction.value
        if x_position == None:
            x_position = 0
            y_position = 0

        # Проверка, что новое направление не выходит за границы карты
        def is_within_bounds(x, y, dx, dy, max_x, max_y):
            return 0 <= x + dx < max_x and 0 <= y + dy < max_y

        # Если текущий путь не выводит за границы карты
        if is_within_bounds(x_position, y_position, dx, dy, max_x, max_y):
            # Вероятность того, что направление не изменится
            keep_direction_probability = strength / 100.0
            if random.random() < keep_direction_probability:
                return direction  # Оставляем текущее направление
        # Иначе нужно выбрать новое направление
        possible_directions = list(Direction)
        possible_directions.remove(
            direction
        )  # Убираем текущее направление из возможных

        valid_directions = [
            d
            for d in possible_directions
            if is_within_bounds(
                x_position, y_position, d.value[0], d.value[1], max_x, max_y
            )
        ]

        # Возвращаем случайное направление, которое не выходит за границы карты
        return random.choice(valid_directions) if valid_directions else direction

    @staticmethod
    def find_direction(a, b):
        x_diff = a[0] - b[0]
        y_diff = a[1] - b[1]

        if x_diff > 0:
            return Direction.RIGHT
        elif x_diff < 0:
            return Direction.LEFT
        elif y_diff > 0:
            return Direction.UP
        elif y_diff < 0:
            return Direction.DOWN
        else:
            return None
