from random import choice, randint

from src.resources.constants import COLOR_CHOICES
from src.resources.entities.level import Level

from .Enemy import Enemy


class EnemyManager:
    """Manager class to add, update, and draw enemy"""

    def __init__(self, level: Level):
        self.enemy_list = []
        self.level = level

    def spawn_random_enemies(self, x_player: int, y_player: int, num: int) -> None:
        """Spawns a new enemies randomly"""
        selected = []
        color = ''
        found_color = False
        while num > 0:
            while not found_color:
                color = choice(COLOR_CHOICES)
                if color not in selected:
                    found_color = True
                    selected.append(color)
            y = randint(2, self.level.height-2)
            x = randint(2, self.level.width-2)
            disallowed_spaces = {'x': (x_player - 1, x_player + 1), 'y': (y_player - 1, y_player + 1)}
            if str(self.level.board[y][x]) == "'" and \
                    x not in disallowed_spaces['x'] and y not in disallowed_spaces['y']:
                num -= 1
                enemy = Enemy(aggro_radius=3, x=x, y=y, symbol='^', color=color)
                self.enemy_list.append(enemy)

    def collisions_with_player(self, x: int, y: int) -> bool:
        """Checks if player collided with enemy"""
        return any([(enemy.x, enemy.y) == (x, y) for enemy in self.enemy_list])
