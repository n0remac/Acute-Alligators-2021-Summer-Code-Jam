from random import choice

from .AbstractDungeonEntity import AbstractDungeonEntity


class Enemy(AbstractDungeonEntity):
    """Enemy entity and hostile to players"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self) -> None:
        """Update enemy"""
        self.mill()
        self.player_in_radius()

    def mill(self) -> None:
        """Enemy randomly moves around"""
        movement_axis = choice(['x', 'y'])
        direction_axis = [1, -1]
        movement = choice(direction_axis)  # up or down (1, -1), left or right (1, -1)
        if movement_axis == 'x':  # movement will be on the x axis
            if (self.x <= 1 and movement == -1) or (self.x >= self.level.width - 2 and movement == 1):
                direction_axis.remove(movement)
                self.x += int(direction_axis[0])
            else:
                self.x += movement
        if movement_axis == 'y':  # movement will be on the y axis
            if (self.y <= 1 and movement == -1) or (self.y >= self.level.height - 2 and movement == 1):
                direction_axis.remove(movement)
                self.y += int(direction_axis[0])
            else:
                self.y += movement

    def player_in_radius(self) -> None:
        """Checks if the player is in the 'aggro' radius of the enemy"""
        board = self.level.board
        spaces_next_to_enemy = [board[self.x + 1][self.y], board[self.x - 1][self.y],  # horizontal
                                board[self.x][self.y + 1], board[self.x][self.y - 1],  # vertical
                                board[self.x + 1][self.y - 1], board[self.x - 1][self.y - 1],  # horizontal diagonal
                                board[self.x - 1][self.y + 1], board[self.x + 1][self.y + 1]]  # vertical diagonal
        if "$" in str(spaces_next_to_enemy):
            self.symbol.stylize("bold red")
        else:
            self.symbol.stylize("bold white")

    def draw(self) -> None:
        """Places entity on map"""
        self.level.board[self.x][self.y] = self.ground_symbol
        self.update()
        self.level.board[self.x][self.y] = self.symbol
