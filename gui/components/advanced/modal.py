from ...core import View, Renderer
from ..label import Label
from ..button import Button
from ...utils import log_event
from typing import List


class Modal(View[None]):
    """
    A modal dialog component.
    """

    def __init__(
        self,
        x: int,
        y: int,
        width: int = 400,
        height: int = 300,
        title: str = "Modal",
        buttons: List[Button] = None,
    ):
        """
        Initializes a modal dialog component.

        :param x: The x-coordinate of the modal.
        :param y: The y-coordinate of the modal.
        :param width: The width of the modal. Default is 400.
        :param height: The height of the modal. Default is 300.
        :param title: The title of the modal. Default is "Modal".
        :param buttons: A list of buttons for actions. Default is None.
        """
        super().__init__(x, y, width, height)
        self._title_label = Label(10, 10, width - 20, 40, text=title)
        self._buttons = buttons or []

    @log_event
    def render(self, renderer: Renderer) -> None:
        """
        Renders the modal and its elements.

        :param renderer: The renderer responsible for drawing the modal.
        """
        self.apply_modifiers()
        renderer.render_modal(self)
        self._title_label.render(renderer)
        for button in self._buttons:
            button.render(renderer)

    def add_button(self, button: Button) -> 'Modal':
        """
        Adds a button to the modal.

        :param button: The button to add.
        :return: Self for chaining.
        """
        self._buttons.append(button)
        return self
