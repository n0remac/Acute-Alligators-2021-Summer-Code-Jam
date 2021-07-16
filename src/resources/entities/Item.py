from .AbstractDungeonEntity import AbstractDungeonEntity
from .level.Tile import Tile


class Item(AbstractDungeonEntity):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.collected = False

    def collisions_with_player(self, x: int, y: int) -> bool:
        """Checks if player collided with enemy"""
        return (self.x, self.y) == (x, y)

    def collect_item(self, board):
        self.collected = True
        board[self.y][self.x] = Tile(text="''", style="bold magenta")
