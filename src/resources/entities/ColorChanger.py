from .AbstractDungeonEntity import AbstractDungeonEntity
from .character import Character


class ColorChanger(AbstractDungeonEntity):
    """Dungeon Items that change players color if captured"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def collisions_with_player(self, x: int, y: int) -> bool:
        """Checks if player collided with enemy"""
        return ((self.x, self.y) == (x, y-1)) or ((self.x, self.y) == (x-1, y))

    def _reset(self) -> None:
        """Resets symbol to normal game 'tick'"""
        self.symbol = self.ground_symbol

    def change_color(self, player: Character) -> None:
        """Will change color of player instance and reset to normal game tile"""
        player.symbol.stylize(self.style)
        self._reset()
