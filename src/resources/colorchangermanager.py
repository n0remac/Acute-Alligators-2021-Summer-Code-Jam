from random import randint
from typing import Optional

from .entities.character import Character
from .entities.ColorChanger import ColorChanger
from .entities.EnemyManager import EnemyManager
from .Level import Level


class ColorChangerManager:
    """Manager class to add, update, and draw enemy"""

    def __init__(self, level: Level):
        self.color_changer_list = []
        self.level = level

    def spawn_color_changer_items(self, x_player: int, y_player: int, num: int) -> None:
        """Spawns a new enemies randomly"""
        while num > 0:
            y = randint(2, self.level.height-2)
            x = randint(2, self.level.width-2)
            disallowed_spaces = {'x': (x_player - 1, x_player + 1), 'y': (y_player - 1, y_player + 1)}

            if str(self.level.board[y][x]) == "'" and \
                    x not in disallowed_spaces['x'] and y not in disallowed_spaces['y']:
                num -= 1
                enemy = ColorChanger(level=self.level, x=x, y=y, symbol='@', color='yellow')
                self.color_changer_list.append(enemy)

    def update(self, enemy_manager: EnemyManager, player: Character) -> None:
        """Updates color changer items"""
        player_collided, color_changer_used = self.collisions_with_player(player.x, player.y)
        if player_collided:
            self.reset(player.x, player.y)

    def reset(self, x: int, y: int) -> None:
        """Update each enemy in enemy list"""
        for color_changer in self.color_changer_list:
            if color_changer.x == x and color_changer.y == y:
                color_changer.reset()

    def collisions_with_player(self, x: int, y: int) -> tuple[bool, Optional[tuple[int, int]]]:
        """Checks if player collided with enemy"""
        x_y_coords = [(color_changer.x, color_changer.y) for color_changer in self.color_changer_list]
        return any((equality := [i == (x, y) for i in x_y_coords])), \
            x_y_coords[equality.index(True)] if True in equality else None

    def draw(self) -> None:
        """Draw each enemy in enemy list"""
        for color_changer in self.color_changer_list:
            color_changer.draw()
