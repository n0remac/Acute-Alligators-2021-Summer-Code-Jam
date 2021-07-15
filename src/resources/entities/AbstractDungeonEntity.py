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
            self.symbol.stylize(color)

    def __gt__(self, obj: type) -> bool:
        """Return True if current object is greater than"""
        if self.symbol.style == "bold red" and self.symbol.style == "bold green":
            state = True
        elif self.symbol.style == "bold green" and self.symbol.style == "bold blue":
            state = True
        elif self.symbol.style == "bold blue" and self.symbol.style == "bold red":
            state = True
        else:
            state = False
        return state

    def __le__(self, obj: type) -> bool:
        """Returns True if current object is less than"""
        if self.symbol.style == "bold green" and self.symbol.style == "bold red":
            state = True
        elif self.symbol.style == "bold blue" and self.symbol.style == "bold green":
            state = True
        elif self.symbol.style == "bold red" and self.symbol.style == "bold blue":
            state = True
        else:
            state = False
        return state

    def __eq__(self, obj: type) -> bool:
        """Compares AbstractEntityObjects for equality"""
        return self.symbol.style == obj.symbol.style

    def __ne__(self, obj: type) -> bool:
        """Compare AbstractEntityObjects for inequaulity"""
        return self.symbol.style != obj.symbol.style
