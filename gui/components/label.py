from ..core import View, Renderer
from ..utils import log_event


class Label(View[str]):
    """
    A simple label component for displaying text, where state is modified via modifiers.
    """

    def __init__(
        self,
        x: int,
        y: int,
        width: int = 200,
        height: int = 50,
        text: str = "Label",
    ):
        """
        Initializes a label component.

        :param x: The x-coordinate of the label.
        :param y: The y-coordinate of the label.
        :param width: The width of the label. Default is 200.
        :param height: The height of the label. Default is 50.
        :param text: The initial text of the label.
        """
        super().__init__(x, y, width, height)
        self.state = text  # The state stores the current text value

    @log_event
    def render(self, renderer: Renderer) -> None:
        """
        Renders the label using the provided renderer.

        :param renderer: The renderer responsible for drawing the label.
        """
        self.apply_modifiers()  # Apply all modifiers before rendering
        renderer.render_label(self)

    def set_text(self, text: str) -> 'View':
        """
        Sets the text value in the state.

        :param text: The new text value.
        :return: Self for chaining.
        """
        self.state = text
        return self
