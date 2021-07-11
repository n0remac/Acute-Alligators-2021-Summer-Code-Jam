from .base import DungeonBase

class Character(DungeonBase):
    """This describes a character"""

    def update(self, direction: ()) -> None:
        """Takes a direction and updates the player position"""
        if direction:
            # this positon check needs to be refactored.
            if self.x + direction[0] <= 9 and self.x + direction[0] >= 0:
                self.x += direction[0]
            if self.y + direction[1] <= 9 and self.y + direction[1] >= 0:
                self.y += direction[1]


