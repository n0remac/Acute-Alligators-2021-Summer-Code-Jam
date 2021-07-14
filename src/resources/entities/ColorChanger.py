from .AbstractDungeonEntity import AbstractDungeonEntity
from .character import Character


class ColorChanger(AbstractDungeonEntity):
    """Dungeon Items that change players color if captured"""

    def __init__(self, color: str = "yellow", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = color
        self.symbol.stylize(self.color)

    def check_for_collision(self, player: Character) -> None:
        """Compares player's location to Dungeon Item"""
        pass

    def reset(self) -> None:
        """Resets symbol to normal game 'tick'"""
        self.used_items.append(self.symbol)
        self.symbol = "'"
        self.symbol.stylize = "magenta"
