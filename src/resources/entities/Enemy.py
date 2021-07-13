from random import choice

from .AbstractDungeonEntity import AbstractDungeonEntity


class Enemy(AbstractDungeonEntity):
    """Enemy entity and hostile to players"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self, x: int, y: int) -> None:
        """Update enemy"""
        self.level.board[self.y][self.x] = self.ground_symbol
        self.move(self.player_in_radius(x, y), x, y)

    def move(self, player_detected: bool, x: int, y: int) -> None:
        """Enemy movement function"""
        if player_detected:
            distance_from_player = (x - self.x, y - self.y)
            if any([i in (1, -1) for i in distance_from_player]):
                self.x += distance_from_player[0]
                self.y += distance_from_player[1]
            else:
                self.x += distance_from_player[0] - (1 if distance_from_player[0] > 0 else -1)
                self.y += distance_from_player[1] - (1 if distance_from_player[1] > 0 else -1)

        else:
            movement_axis = choice(['x', 'y'])
            direction_axis = (1, -1)
            movement = choice(direction_axis)  # up or down (1, -1), left or right (1, -1)
            if movement_axis == 'x':  # movement will be on the x axis
                if (self.x <= 1 and movement == -1) or (self.x >= self.level.width - 2 and movement == 1):
                    self.x += 1 if movement == -1 else -1
                else:
                    self.x += movement
            if movement_axis == 'y':  # movement will be on the y axis
                if (self.y <= 1 and movement == -1) or (self.y >= self.level.height - 2 and movement == 1):
                    self.y += 1 if movement == -1 else -1
                else:
                    self.y += movement

    def player_in_radius(self, x: int, y: int) -> bool:
        """Check if player is in 'aggro' radius"""
        if (y - 2 <= self.y <= y + 2) or (x - 2 <= self.x <= x + 2):
            self.symbol.stylize("bold red")
            return True
        else:
            self.symbol.stylize("bold white")
            return False

    def draw(self) -> None:
        """Places entity on map"""
        self.level.board[self.y][self.x] = self.symbol
