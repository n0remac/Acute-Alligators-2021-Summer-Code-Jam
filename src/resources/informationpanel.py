from rich.panel import Panel
from rich.text import Text

from .GameResources import GameResources


class Information:
    """Information panel class"""

    def __init__(self, game_resources: GameResources) -> None:
        self.enemy_manager = game_resources.enemy_manager

    def update_panel(self) -> list:
        """Update information panel"""
        enemies_formatted = '\n'.join([f'Enemy {i.file}' for i in self.enemy_manager.enemy_in_radius])
        enemy_info = Text(enemies_formatted, style="red")
        enemy_panel = Panel(enemy_info, title=Text("Enemies that have detected you:"))

        return enemy_panel
