import tkinter as tk
from typing import Protocol

from simulation.core.configs import settings


class Presenter(Protocol):
    def start_handler(self, event=None) -> None: ...


class TkinterView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulation Game")
        self.height = settings.MAP_HEIGHT
        self.width = settings.MAP_WIDTH

    def init_ui(self, presenter: Presenter):
        # Фреймы для меню и карты
        self.menu_frame = tk.Frame(self, padx=10, pady=10)
        self.map_frame = tk.Frame(self)

        self.menu_frame.pack()

        # Заголовок меню
        title_label = tk.Label(
            self.menu_frame, text="Меню Старта Игры", font=("Arial", 16)
        )
        title_label.pack(pady=10)

        # Кнопка старта
        start_button = tk.Button(
            self.menu_frame, text="Начать новую игру", command=presenter.start_handler
        )
        start_button.pack(pady=5)

        # Кнопка выхода
        exit_button = tk.Button(self.menu_frame, text="Выйти", command=self.quit)
        exit_button.pack(pady=5)

    def render_map(self, map_dto: dict):
        # Установка фрейма карты
        self.map_frame.pack()

        # Очистка предыдущих виджетов карты
        for widget in self.map_frame.winfo_children():
            widget.destroy()

        # Создание виджетов карты на основе DTO
        for y in range(self.height):
            for x in range(self.width):
                entity_info = map_dto.get((x, y))

                # Определение содержимого и цвета ячейки
                if entity_info is None:
                    label_text = "."
                    label_color = "white"
                else:
                    label_text = entity_info["name"][0]  # Первая буква названия
                    label_color = "green" if entity_info["name"] == "Grass" else "blue"

                # Отображение ячейки
                cell_label = tk.Label(
                    self.map_frame,
                    text=label_text,
                    width=2,
                    height=1,
                    bg=label_color,
                    borderwidth=1,
                    relief="solid",
                )
                cell_label.grid(row=y, column=x)


# Пример использования:
# game = Game()  # Экземпляр игры Game
# view = TkinterView(game)
# view.start()
