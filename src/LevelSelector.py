from .fstree.FileStructureTree import FileStructureTree


class LevelSelector:
    """Creates and stores levels"""

    def __init__(self):
        self.file_structure = FileStructureTree(".")
