from random import randint

from src.resources.entities.level import Level

from .Enemy import Enemy


class EnemyManager:
    """Manager class to add, update, and draw enemy"""

    def __init__(self, level: Level):
        self.enemy_list = []
        self.level = level

    def spawn_random_enemies(self, x_player: int, y_player: int, files_in_dir: list) -> None:
        """Spawns a new enemies randomly"""
        num = len(files_in_dir) - 1
        while num + 1 > 0:
            y = randint(2, self.level.height-2)
            x = randint(2, self.level.width-2)
            disallowed_spaces = {'x': (x_player - 1, x_player + 1), 'y': (y_player - 1, y_player + 1)}
            if str(self.level.board[y][x]) == "'" and \
                    x not in disallowed_spaces['x'] and y not in disallowed_spaces['y']:
                num -= 1
                enemy = Enemy(aggro_radius=3, x=x, y=y, symbol='^', file=files_in_dir[num])
                self.enemy_list.append(enemy)

    def collisions_with_player(self, x: int, y: int) -> bool:
        """Checks if player collided with enemy"""
        return any([(enemy.x, enemy.y) == (x, y) for enemy in self.enemy_list])
