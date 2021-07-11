from .character import Character 
from .base import DungeonBase

class DungeonItem(DungeonBase):
    used_items = []
    unused_items = []

    def __init__(self,*args):
        super().__init__(*args)
        

    def check_for_collision(self, player):
        # if player location is the same
        # set player to color 
        # delete item
        pass