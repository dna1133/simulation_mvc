from __future__ import annotations

import os
import time
from typing import Protocol

from simulation.app.game import Game
from simulation.core.configs import settings


class View(Protocol):
    def init_ui(self, presenter: Presenter) -> bool: ...
    def render_map(self, map_dto: dict) -> None: ...


class Presenter:
    def __init__(self, game: Game, view: View) -> None:
        self.game = game
        self.view = view

    def start_game(self):
        self._clear()
        self.view.init_ui(self)

    def start_handler(self, event=None) -> None:
        self._start_game()

    def _game_step(self):
        self.game.next_turn()
        time.sleep(settings.TIME_TO_TICK)

    def _render_map(self):
        self.view.render_map(self.game.current_state_to_dto(self.game.map_obj))
        time.sleep(4)

    def _event_loop(self):
        while not self.game.paused:
            self._game_step()
            self._render_map()

    def _start_game(self):
        self.game.start_game()
        time.sleep(1)
        self._event_loop()

    def _clear(self) -> None:
        if os.name == "nt":  # For Windows
            os.system("cls")
        else:  # For Linux and MacOS
            os.system("clear")
