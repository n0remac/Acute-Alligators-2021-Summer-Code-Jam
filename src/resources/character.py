from threading import Thread

from blessed import Terminal
from rich.text import Text

from .level import Level

# Used to get player input
term = Terminal()


class Character:
    """This describes a character"""

    def __init__(self, current_level: Level, symbol: str = "$") -> None:
        self.current_level = current_level
        self.x = current_level.width // 2
        self.y = current_level.height // 2
        self.symbol = Text(symbol)
        self.ground_symbol = current_level.board[self.y][self.x]
        self.playing = True

    def start(self) -> None:
        """Starts the movement controls in a separate thread"""
        Thread(target=self.keyboard_input, args=()).start()

    def keyboard_input(self) -> None:
        """Reads keyboard input and moves the player"""
        on = True
        while on:
            with term.cbreak():  # set keys to be read immediately
                inp = term.inkey()  # wait and read one character
                self.current_level.board[self.y][self.x] = self.ground_symbol
                if inp == "a":
                    if self.x > 1:
                        self.x -= 1
                if inp == "d":
                    if self.x < self.current_level.width - 2:
                        self.x += 1
                if inp == "w":
                    if self.y > 1:
                        self.y -= 1
                if inp == "s":
                    if self.y < self.current_level.height - 2:
                        self.y += 1
                if inp == "p":
                    on = False
                    self.playing = False
                self.ground_symbol = self.current_level.board[self.y][self.x]

    def draw(self) -> None:
        """Places player on map"""
        self.current_level.board[self.y][self.x] = self.symbol
