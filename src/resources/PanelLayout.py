from rich.layout import Layout


class PanelLayout:
    """Define panel layout"""

    @classmethod
    def make_layout(self, start: bool) -> Layout:
        """Makes the layout"""
        if not start:
            layout = Layout(name="root")

            layout.split_row(
                Layout(name="main", ratio=6),
                Layout(name="tree", ratio=2),
            )

            layout['main'].split_column(
                Layout(name='main_game', ratio=7),
                Layout(name='footer', ratio=2)
            )
        else:
            layout = Layout(name="start")

        layout['footer'].split_column(
            Layout(name="player_health", ratio=3),
            Layout(name="display_enemies", ratio=6)
        )

        return layout
