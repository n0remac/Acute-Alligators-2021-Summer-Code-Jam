from time import sleep

from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.layout import Layout

from src.resources.items import DungeonItem
from src.resources.character import Character
from src.resources.level import Level


def run_game(layout: Layout) -> Panel:
    """
    This function in in charge of running the game. It will call update and draw for each game object.

    Layout: Layout  Holds all the rich renderables for the game. Updated with a new panel each tick.
    """

    player.draw()
    dungeon_item.draw(level.board)
    panel = Panel(level.to_string())
    layout.update(panel)
    sleep(0.1)
    return panel


# This a temporary home for these game objects. they should be moved to a better place.
level = Level(10, 5, [1, 2, 3, 4], [])
player = Character(level, "$")
player.start()

dungeon_item = DungeonItem(5, 5, "@", "green")

game_panel = Panel(level.to_string())
layout = Layout(game_panel)

with Live(layout, refresh_per_second=10, screen=True):
    while player.playing:
        run_game(layout)
