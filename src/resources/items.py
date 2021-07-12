from .base import DungeonBase
from .character import Character


class DungeonItem(DungeonBase):
    """Dungeon Items that change players color if captured"""

    used_items = []
    unused_items = []

    def __init__(self, *args):
        super().__init__(*args)

    def check_for_collision(self, player: Character) -> None:
        """Compares player's location to Dungeon Item"""
        pass

    def reset(self) -> None:
        """Resets symbol to normal game 'tick'"""
        self.used_items.append(self.symbol)
        self.symbol = "'"
        self.symbol.stylize = "magenta"
