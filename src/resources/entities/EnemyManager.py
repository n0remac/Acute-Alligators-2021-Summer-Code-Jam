from ..Level import Level
from .Enemy import Enemy


class EnemyManager:
    """Manager class to add, update, and draw enemy"""

    def __init__(self, level: Level):
        self.enemy_list = []
        self.level = level

    def spawn_enemy(self) -> None:
        """Spawns a new enemy"""
        enemy = Enemy(level=self.level)
        self.enemy_list.append(enemy)

    def update(self) -> None:
        """Update each enemy in enemy list"""
        for enemy in self.enemy_list:
            enemy.update()

    def draw(self) -> None:
        """Draw each enemy in enemy list"""
        for enemy in self.enemy_list:
            enemy.draw()
