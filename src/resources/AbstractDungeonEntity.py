from rich.text import Text


class AbstractDungeonEntity:
    """Base class to set items color and location"""

    _entity_positions = {}

    def __init__(self, ground_symbol: str = "'", x: int = 0, y: int = 0, symbol: str = "$", color: str = '', ):
        self.x = x
        self.y = y
        self.symbol = Text(symbol)
        self.ground_symbol = ground_symbol
        if color:
            self.symbol.stylize(color)

    def draw(self, level: list) -> None:
        """Places object on map"""
        level[self.x][self.y] = self.symbol
        self._set_position()
        return level

    def _set_position(self) -> None:
        """Sets or updates position of entity"""
        self._entity_position[self.__class__] = (self.x, self.y)

    def __getattribute__(self, attr: str) -> None:
        """Prohibits access to main entity positions"""
        if attr == '_entity_postitions':
            return (self.x, self.y)
        else:
            return object.__getattribute__(self, attr)
