from pynput.keyboard import Key, Listener

from .PanelLayout import PanelLayout


class StartScreen:
    """Start screen of game"""

    def __init__(self) -> None:
        self.layout = PanelLayout.make_layout(start=True)
        self.guide = False
        self.in_start = True

    def press(self, key: Key) -> None:
        """Reads keyboard input"""
        try:
            print(key.char)
            if key.char == 'h':
                self.guide = True
            if key.char == 'b' and self.guide is True:
                self.guide = False
            if key.char == 's':
                self.in_start = False
        except AttributeError:
            self.in_start = False

    def release(self, key: Key) -> bool:
        """On key release"""
        return False

    def keyboard_input(self) -> None:
        """Uses listener that reads keyboard input from press"""
        with Listener(on_press=self.press, on_release=self.release) as listener:  # set keys to be read immediately
            listener.join()
