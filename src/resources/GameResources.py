from time import sleep

from .colorchangermanager import ColorChangerManager
from .entities.character import Character
from .entities.EnemyManager import EnemyManager
from .Level import Level


class GameResources:
    """holds objects that are used for during game runtime"""

    def __init__(self):
        self.level = Level(20, 15, [1, 2, 3, 4], [])
        self.player = Character(self.level, "$")
        self.color_manager = ColorChangerManager(level=self.level)
        self.enemy_manager = EnemyManager(self.level)
        # self.enemy_manager.spawn_random_enemies(self.player.x, self.player.y, 6)
        self.color_manager.spawn_color_changer_items(self.player.x, self.player.y, 2)

    def update(self) -> None:
        """Updates all game objects"""
        self.player.keyboard_input()
        self.enemy_manager.update(self.player.x, self.player.y)
        self.color_manager.update(self.enemy_manager, self.player)

    def draw(self) -> bool:
        """
        Function to draw entities in game resources class.

        The last drawn entities will appear on top of ones before it.
        """
        self.player.draw()
        if self.enemy_manager.collisions_with_player(self.player.x, self.player.y):
            self.player.playing = False
        else:
            self.enemy_manager.draw()
            self.color_manager.draw()
            sleep(0.1)
            return True
