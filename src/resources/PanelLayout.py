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
            layout = Layout(name="start_screen")

            layout.split_column(
                Layout(name="start", ratio=6),
                Layout(name="loading", ratio=2),
            )

        return layout
