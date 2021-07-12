from .entities.character import Character
from .level import Level


class GameResources:
    """holds objects that are used for during game runtime"""

    def __init__(self):
        self.level = Level(10, 10, [1, 2, 3, 4], [])
        self.player = Character(self.level, "$")
        self.player.start()
