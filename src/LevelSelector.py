from .fstree.FileStructureTree import FileStructureTree
from .resources.entities.level.Level import Level


class LevelSelector:
    """Creates and stores levels"""

    def __init__(self):
        self.file_structure = FileStructureTree(".")
        self.cur = self.file_structure.root

    def create_level(self, door: (int, int) = (0, 0)) -> Level:
        """Creates a Level"""

        level = Level(10, 15, self.cur)
        level.generate_level()
        level.create_doors(door)
        level.cur_node = self.cur

        return level
