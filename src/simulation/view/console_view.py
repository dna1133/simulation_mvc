from typing import Protocol
from simulation.core.configs import settings


class Presentor(Protocol):
    def start_handler(self, event=None) -> None: ...


class ConsoleView:
    def __init__(self):
        self.height: int = (settings.MAP_HEIGHT,)
        self.width: int = (settings.MAP_WIDTH,)

    def init_ui(self, presenter: Presentor):
        print("===== Меню Старта Игры =====")
        print("1. Начать новую игру")
        print("2. Выйти")

        choice = input("Выберите действие (1 или 2): ")
        if choice == "1":
            print("Игра началась!")
            presenter.start_handler()
        elif choice == "2":
            print("Выход из игры.")
            exit()
        else:
            print("Неверный ввод. Попробуйте снова.")
            self.init_ui()  # Повторный вывод меню, если ввод неверный

    def render_map(
        self,
        map_dto: dict,
        height: int = settings.MAP_HEIGHT,
        width: int = settings.MAP_WIDTH,
    ):
        # Получаем DTO-карту

        print("\n===== Карта =====")
        for y in range(height):
            row = ""
            for x in range(width):
                entity_info = map_dto.get((x, y))
                if entity_info is None:
                    row += settings.ENTITY_IMG["Default"]
                else:
                    row += settings.ENTITY_IMG[entity_info["name"]]
            print(row)
        print("====================\n")
