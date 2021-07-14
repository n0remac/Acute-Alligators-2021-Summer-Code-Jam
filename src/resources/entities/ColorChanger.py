from rich.text import Text

from .AbstractDungeonEntity import AbstractDungeonEntity


class ColorChanger(AbstractDungeonEntity):
    """Dungeon Items that change players color if captured"""

    def __init__(self, color: str = "yellow", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = color
        self.symbol.stylize(self.color)

    def reset(self) -> None:
        """Resets color changer to used item once player collides"""
        self.symbol = Text("@", style="bold grey")
