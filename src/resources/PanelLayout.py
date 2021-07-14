from rich.layout import Layout


class PanelLayout:
    """Define panel layout"""

    def __init__(self) -> None:
        pass

    def make_layout() -> Layout:
        """Makes the layout"""
        layout = Layout(name="root")

        layout.split_row(
            Layout(name="main", ratio=6),
            Layout(name="tree", ratio=2),
        )

        layout['main'].split_column(
            Layout(name='main game', ratio=7),
            Layout(name='footer', ratio=2)
        )

        return layout
