from rich.text import Text


class DungeonBase:

    def __init__(self, x: int = 0, y: int = 0, symbol: str = "$", color:str=''):
        self.x = x
        self.y = y
        self.symbol = Text(symbol)
        if color:
            self.symbol.stylize(color)

    def draw(self, level: list) -> None:
        """Places object on map"""
        level[self.x][self.y] = self.symbol
        return level