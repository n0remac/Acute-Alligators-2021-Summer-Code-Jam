from .fstree.FileStructureTree import FileStructureTree
from .resources.entities.level.Level import Level

class LevelSelector:
    """Creates and stores levels"""

    def __init__(self):
        self.file_structure = FileStructureTree(".")
        self.cur = self.file_structure.root

    def create_level(self):
        return Level(12, 12, self.cur.children)

    def get_num_children(self):
        return len(self.cur.children)
