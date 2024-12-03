from ...utils import Observable
from .radiobutton import RadioButton


class RadioGroup(Observable):
    """
    A group of radio buttons, ensuring only one can be selected at a time.
    """

    def __init__(self):
        super().__init__()
        self._buttons = []

    def add_button(self, button: RadioButton) -> None:
        """
        Adds a radio button to the group.

        :param button: The radio button to add.
        """
        self._buttons.append(button)

    def select(self, button: RadioButton) -> None:
        """
        Selects a radio button and deselects others in the group.

        :param button: The radio button to select.
        """
        for btn in self._buttons:
            btn.state = btn == button
        self.notify_observers(selected_value=button.value)
