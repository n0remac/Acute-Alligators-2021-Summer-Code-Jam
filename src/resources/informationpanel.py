from rich.panel import Panel
from rich.text import Text

from .GameResources import GameResources


class Information:
    """Information panel class"""

    def __init__(self, game_resources: GameResources) -> None:
        self.enemy_manager = game_resources.enemy_manager
        self.default_panel = Panel(Text("No enemies have detected you yet.", style="bold green"))

    def update_panel(self) -> list:
        """Update information panel"""
        enemy_panels = []
        for enemy in self.enemy_manager.enemy_in_radius:
            enemy_info = Text("attrs go here..", style="red")
            enemy_panel = Panel(enemy_info, title=Text(f"Enemy {enemy.file}", style="bold magenta"))
            enemy_panels.append(enemy_panel)

        return enemy_panels
