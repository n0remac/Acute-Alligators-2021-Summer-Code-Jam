import sys
from time import sleep

from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

from src.GameResources import GameResources
from src.resources.informationpanel import Information
from src.resources.PanelLayout import PanelLayout
from src.resources.startscreen import StartScreen


def start_screen() -> None:
    """Start screen"""
    screen = StartScreen()
    layout_screen = screen.layout
    layout_screen.update(
        screen.display_screen()
    )

    with Live(layout_screen, refresh_per_second=10, screen=True):
        while screen.in_start:
            screen.keyboard_input()
            # start screen
            if screen.guide is True:
                layout_screen.update(
                    screen.display_guide()
                )
            else:
                layout_screen.update(
                    screen.display_screen()
                )

    # loading bar once 's' is pressed
    screen.loading_bar()


def end_screen(layout: Layout) -> None:
    """Displays game over screen"""
    with open('ascii.txt', 'r') as file:
        panel = Panel(Text(''.join(file.readlines()), style="bold red", justify='full'))
        layout["main_game"].update(panel)
        layout["footer"].split_column((Panel(Text("Nice try.", style="bold red"))))
        sleep(3)


def run_game(layout: Layout, information: Information, game_resources: GameResources) -> Panel:
    """
    This function in in charge of running the game. It will call update and draw for each game object.

    Layout: Layout  Holds all the rich renderables for the game. Updated with a new panel each tick.
    """
    game_resources.update(bless)
    game_resources.draw()
    enemies_in_radius = information.update_panel()
    panel = Panel(game_resources.level.to_string())

    # Panels to update
    layout["main_game"].update(panel)
    layout["player_health"].split_row(information.get_player_health())
    if enemies_in_radius:
        layout["display_enemies"].split_row(enemies_in_radius)
    else:
        layout["display_enemies"].split_row(information.enemy_default_panel)
    layout["tree"].update(
        Panel(game_resources.node.display_node(), title="Current Location")
    )
    sleep(0.1)


def main() -> None:
    """Main function that sets up game and runs main game loop"""
    game_resources = GameResources(testing, bless)
    information = Information(game_resources)
    game_resources.draw()

    game_panel = Panel(game_resources.level.to_string())
    layout = PanelLayout.make_layout(start=False)
    layout["main_game"].update(game_panel)

    # Panels to update
    layout["player_health"].split_row(Panel(Text("100 HP", style="green")))
    layout["display_enemies"].split_row(information.update_panel())
    layout["tree"].update(
        Panel(game_resources.node.display_node(), title="Current Location")
    )

    start_screen()

    with Live(layout, refresh_per_second=10, screen=False):
        while game_resources.player.playing:
            run_game(layout, information, game_resources)
        end_screen(layout)


testing = False
bless = False
if __name__ == "__main__":
    if sys.argv[-1] == "--test":
        testing = True
    elif sys.argv[-1] == "--bless":
        bless = True
    main()
