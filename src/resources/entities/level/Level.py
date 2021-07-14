from random import randint

from rich.text import Text

from .Door import Door
from .Tile import Tile
from .Wall import Wall


class Level:
    """Generates and contains a level"""

    def __init__(self, width: int, height: int, children: list, files: list) -> None:
        self.board = []
        self.width = width
        self.height = height
        self.door = Door(text="#", style="bold green")
        self.generate_level(width, height)
        self.set_border()
        self.add_doors(len(children))

    def generate_level(self, x: int, y: int) -> None:
        """Generates level"""
        for j in range(y):
            row = []
            for i in range(x):
                tile = Tile(text="'", style="bold magenta")
                row.append(tile)
            self.board.append(row)

    def add_doors(self, doors: int) -> None:
        """Add doors to level"""
        while doors:
            direction: int = randint(0, doors) % 3
            x: int = 0
            y: int = 0
            if direction == 2:
                y = randint(1, self.height - 2)
                x = self.width - 1
            if direction == 1:
                x = randint(1, self.width - 2)
                y = self.height - 1
            if direction == 0:
                y = randint(1, self.height - 2)
                x = 0

            if self.board[y][x] != self.door:
                self.board[y][x] = self.door
                doors -= 1

    def set_border(self) -> None:
        """Creates a walls around the level"""
        for i in range(self.width):
            self.board[0][i] = Wall(text="═", style="bold white")
            self.board[self.height - 1][i] = Wall(text="═", style="bold white")
        for i in range(self.height):
            self.board[i][0] = Wall(text="║", style="bold white")
            self.board[i][self.width - 1] = Wall(text="║", style="bold white")
        self.board[0][0] = Wall(text="╔", style="bold white")
        self.board[self.height - 1][0] = Wall(text="╚", style="bold white")
        self.board[0][self.width - 1] = Wall(text="╗", style="bold white")
        self.board[self.height - 1][self.width - 1] = Wall(text="╝", style="bold white")

    def to_string(self) -> Text:
        """Convert map to string"""
        string_map = Text()
        for row in self.board:
            for col in row:
                string_map += col
            string_map += "\n"
        return string_map