from simulation.app.game import Game
from simulation.interfaces.presenter import Presenter
from simulation.view.console_view import ConsoleView
from simulation.view.tk_view import TkinterView


def main() -> None:
    game = Game()
    # view2 = TkinterView()
    view = ConsoleView()
    presenter = Presenter(game, view)
    presenter.start_game()


if __name__ == "__main__":
    main()
