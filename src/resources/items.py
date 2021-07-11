from .character import Character 

class DungeonItem(Character):

    def __init__(self, x, y, symbol, color):
        super().__init__(x, y, symbol)
        self.symbol.stylize(f'bold {color}')

    def check_for_collision(self, player):
        # if player location is the same
        # set player to color 
        # delete item
        pass
