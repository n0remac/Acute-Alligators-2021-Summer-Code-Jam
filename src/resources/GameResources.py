import random

from src.resources.constants import COLOR_CHANGER_CHOICES, PLAYER_COLOR_CHOICES

from ..LevelSelector import LevelSelector
from .entities.AbstractDungeonEntity import AbstractDungeonEntity
from .entities.character import Character
from .entities.ColorChangerManager import ColorChangerManager
from .entities.EnemyManager import EnemyManager


class GameResources:
    """Holds objects that are used for during game runtime"""

    def __init__(self, testing: bool, bless: bool):
        self.level_selector = LevelSelector()

        self.level = self.level_selector.create_level()
        self.player = Character(symbol="$", x=self.level.width // 2, y=self.level.height // 2,
                                color=self._choose_random_color('character'))

        if bless:
            self.player.start()

        self.color_changer_manager = ColorChangerManager(self.level)
        self.enemy_manager = EnemyManager(self.level)

        self.color_changer_manager.spawn_random_changers(self.player.x, self.player.y)
        self.enemy_manager.spawn_random_enemies(self.player.x, self.player.y, 2)
        self.testing = testing

    def update_entity(self, entity: AbstractDungeonEntity) -> None:
        """Updates the position of a single entity"""
        x = entity.new_positions["x"]
        y = entity.new_positions["y"]
        try:
            if str(self.level.board[entity.y + y][entity.x + x]) in ("'", "$", "@", "#", "^"):
                self.level.board[entity.y][entity.x] = entity.ground_symbol
                entity.x += x
                entity.y += y
                entity.ground_symbol = self.level.board[entity.y][entity.x]
                entity.new_positions = {"x": 0, "y": 0}
        except IndexError:
            pass

    def draw_entity(self, entity: AbstractDungeonEntity) -> None:
        """Draws a single entity onto the level"""
        self.level.board[entity.y][entity.x] = entity.symbol

    def update(self, bless: bool) -> None:
        """Updates all game objects"""
        if bless:
            self.player.update()
        else:
            self.player.keyboard_input()

        self.update_entity(self.player)

        # if player walks on door generate new level
        if str(self.level.board[self.player.y][self.player.x]) == "#":
            self.level = self.level_selector.create_level((self.player.y, self.player.x))
            self.player.x = self.level.entrance[1]
            self.player.y = self.level.entrance[0]

        for enemy in self.enemy_manager.enemy_list:
            if enemy.is_in_radius(self.player.x, self.player.y):
                enemy.follow(self.testing)
            else:
                enemy.mill()

            self.update_entity(enemy)

        new_color = self.color_changer_manager.collisions_with_player(self.player.x, self.player.y)
        if new_color:
            self.color_changer_manager.change_color(self.player, new_color)

    def draw(self) -> bool:
        """
        Function to draw entities in game resources class.

        The last drawn entities will appear on top of ones before it.
        """
        self.draw_entity(self.player)

        result = self.enemy_manager.collisions_with_player(self.player)
        if isinstance(result, Character):
            self.player.playing = False
            return False

        else:
            if str(result) != 'draw':
                self.enemy_manager.remove_enemy(result)
            for enemy in self.enemy_manager.enemy_list:
                self.draw_entity(enemy)
            for color_changer in self.color_changer_manager.color_changer_list:
                self.draw_entity(color_changer)

        self.draw_entity(self.player)

    def overlaps(self, first_entity: AbstractDungeonEntity, second_entity: AbstractDungeonEntity) -> bool:
        """Checks if two entities overlap"""
        return first_entity.x == second_entity.x and first_entity.x == second_entity.y

    def _choose_random_color(self, entity: str = None) -> None:
        """Selects random color"""
        if entity == 'character':
            color = random.choice(PLAYER_COLOR_CHOICES)
        else:
            color = random.choice(COLOR_CHANGER_CHOICES)
        return color
