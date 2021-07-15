from rich.text import Text

from .level.LevelResources import LevelResources
from .level.Tile import Tile


class AbstractDungeonEntity:
    """Base class to set items color and location"""

    def __init__(
        self,
        ground_symbol: str = "'",
        y: int = 0,
        x: int = 0,
        symbol: str = "$",
        color: str = "white",
    ):
        super().__init__()
        self.x = x
        self.y = y
        self.symbol = Text(symbol)
        self.ground_symbol: LevelResources = Tile(text=ground_symbol, style="bold magenta")

        self.new_positions: dict = {"x": 0, "y": 0}

        if color:
            self.color = color
            self.symbol.stylize(self.color)

    def __gt__(self, obj: type) -> bool:
        """Return True if current object is greater than"""
        # print('check gt')
        # print('self: {} other: {}'.format(self.color, obj.color))

        if self.color == "bold red" and obj.color == "bold green":
            state = True
        elif self.color == "bold green" and obj.color == "bold blue":
            state = True
        elif self.color == "bold blue" and obj.color == "bold red":
            state = True
        else:
            state = False
        return state

    def __lt__(self, obj: type) -> bool:
        """Returns True if current object is less than"""
        # print('check lt')
        # print('self: {} other: {}'.format(self.color, obj.color))
        if self.color == "bold green" and obj.color == "bold red":
            state = True
        elif self.color == "bold blue" and obj.color == "bold green":
            state = True
        elif self.color == "bold red" and obj.color == "bold blue":
            state = True
        else:
            state = False
        return state

    def __eq__(self, obj: type) -> bool:
        """Compares AbstractEntityObjects for equality"""
        # print('check eq')
        # print('self: {} other: {}'.format(self.color, obj.color))
        return self.color == obj.color

    def __ne__(self, obj: type) -> bool:
        """Compare AbstractEntityObjects for inequaulity"""
        # print('check ne')
        # print('self: {} other: {}'.format(self.color, obj.color))
        return self.color != obj.color
