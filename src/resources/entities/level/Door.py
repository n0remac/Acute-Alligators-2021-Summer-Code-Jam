from .LevelResources import LevelResources


class Door(LevelResources):
    """Creates a Door object"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id: int = 0

    def set_id(self, num):
        self.id = num
