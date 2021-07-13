from random import choice

from .AbstractDungeonEntity import AbstractDungeonEntity
from .character import Character


class Enemy(AbstractDungeonEntity):
    """Enemy entity and hostile to players"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self, character: Character) -> None:
        """Update enemy"""
        self.mill()
        if self.player_in_radius():
            self.chase_player(character)

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

    def chase_player(self, character: Character) -> None:
        """Follows player once detected"""
        distance_from_player = [(character.x - self.x) + 1, (character.y - self.y) + 1]
        if self.x + distance_from_player[0] <= 1 or self.x + distance_from_player[0] >= self.level.width - 1:
            self.x += distance_from_player[0]
        if self.y + distance_from_player[1] <= 1 or self.y + distance_from_player[1] >= self.level.height - 1:
            self.y += distance_from_player[1]

    def player_in_radius(self) -> bool:
        """Checks if the player is in the 'aggro' radius of the enemy"""
        board = self.level.board
        spaces_next_to_enemy = [board[self.x + 1][self.y], board[self.x - 1][self.y],  # horizontal
                                board[self.x][self.y + 1], board[self.x][self.y - 1],  # vertical
                                board[self.x + 1][self.y - 1], board[self.x - 1][self.y - 1],  # horizontal diagonal
                                board[self.x - 1][self.y + 1], board[self.x + 1][self.y + 1]]  # vertical diagonal
        if "$" in str(spaces_next_to_enemy):
            self.symbol.stylize("bold red")
            return True
        else:
            self.symbol.stylize("bold white")
            return False

    def draw(self, character: Character) -> None:
        """Places entity on map"""
        self.level.board[self.x][self.y] = self.ground_symbol
        self.update(character)
        self.level.board[self.x][self.y] = self.symbol
