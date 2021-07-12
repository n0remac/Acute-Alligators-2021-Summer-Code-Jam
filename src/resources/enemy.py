from random import randint

from .AbstractDungeonEntity import AbstractDungeonEntity
from .level import Level


class Enemy(AbstractDungeonEntity):
    """Enemy entity and hostile to players"""

    def __init__(self, current_level: Level, symbol: str = '^') -> None:
        super().__init__(
            ground_symbol=current_level.board[
                (x := randint(2, current_level.width - 2))
            ][(y := randint(2, current_level.height - 2))],
            x=x,
            y=y,
            symbol=symbol
        )
        self.current_level = current_level

    def draw(self) -> None:
        """Draws enemies to board"""
        # while loop to ensure that enemies don't get placed in the same area
        while str(self.current_level.board[self.y][self.x]) in (self.symbol, '$'):
            self.x = randint(2, self.current_level.width - 2)
            self.y = randint(2, self.current_level.width - 2)

        self.current_level.board[self.y][self.x] = self.symbol
