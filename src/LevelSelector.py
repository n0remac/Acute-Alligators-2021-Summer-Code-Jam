from random import choice

from .fstree.FileStructureTree import FileStructureTree
from .resources.entities.level.Level import Level


class LevelSelector:
    """Creates and stores levels"""

    def __init__(self, fsf: FileStructureTree):
        self.file_structure = fsf
        self.cur = self.file_structure.root

    def create_level(self, door: (int, int) = (0, 0), *, game_started: bool) -> None:
        """Creates a Level"""
        if game_started:
            self.cur = choice(self.cur.children)
        level = Level(10, 15, self.cur.children, door)
        return level
