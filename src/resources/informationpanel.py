from rich.panel import Panel
from rich.text import Text

from .GameResources import GameResources


class Information:
    """Information panel class"""

    def __init__(self, game_resources: GameResources) -> None:
        self.enemy_manager = game_resources.enemy_manager
        self.player = game_resources.player
        self.enemy_default_panel = Panel(Text("No enemies have detected you yet.", style="bold green"))

    def update_panel(self) -> list:
        """Update information panel"""
        enemy_info = Text("")
        for enemy in self.enemy_manager.enemy_list:
            text_to_add = f"Enemy {enemy.file} - Attacked you for {enemy.damage_attacked_for} HP\t" \
                if enemy in self.enemy_manager.enemy_in_radius else f"Enemy {enemy.file}\t"
            enemy_info += Text(text_to_add, style="red" if enemy in self.enemy_manager.enemy_in_radius else "white")

        return Panel(enemy_info, title="Enemies")

    def get_player_health(self) -> Panel:
        """Sets panel for player health"""
        health = self.player.health
        hearts = Text(f"{'♥' * (health // 10) if health >= 10 else '♥'}   |   You have: {health}HP", style="bold red")
        health_panel = Panel(hearts, title="Your Health")
        return health_panel
