from time import sleep

from .entities.character import Character
from .entities.ColorChanger import ColorChanger
from .entities.EnemyManager import EnemyManager
from .Level import Level


class GameResources:
    """holds objects that are used for during game runtime"""

    count = 1  # Test

    def __init__(self):
        self.level = Level(20, 15, [1, 2, 3, 4], [])
        self.player = Character(self.level, "$")
        self.test_color_changer = ColorChanger(level=self.level, x=2, y=2, symbol="@", color="green")
        self.enemy_manager = EnemyManager(self.level)
        self.enemy_manager.spawn_random_enemies(self.player.x, self.player.y, 6)

    def update(self) -> None:
        """Updates all game objects"""
        self.player.keyboard_input()
        self.enemy_manager.update(self.player.x, self.player.y)

    def draw(self) -> bool:
        """
        Function to draw entities in game resources class.

        The last drawn entities will appear on top of ones before it.
        """
        self.player.draw()
<<<<<<< HEAD
        if self.enemy_manager.collisions_with_player(self.player.x, self.player.y):
            self.player.playing = False
        else:
            self.enemy_manager.draw()
            self.test_color_changer.draw()
            sleep(0.1)
            return True
=======
        self.test_color_changer.draw()
        self.count += 1  # Test
        if self.count == 4:  # Test
            self.test_color_changer.change_color()  # test

        sleep(0.1)
>>>>>>> WIP: Initiate color change to player objects. Removed __str__ method from LevelResources. Remove draw() from Enemy class to make code more DRY. Added new instance arttr to apply color update
