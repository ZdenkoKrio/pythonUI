from core.view import View
from core.renderer import Renderer
from core.events import Event, EventType
from utils.logging import log_event


class TextBox(View):
    """
    Represents a text box component with default parameters.
    """

    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        width: int = 200,
        height: int = 30,
        placeholder: str = "Enter text...",
    ):
        """
        Initializes a text box component with default parameters.

        :param x: The x-coordinate of the text box. Default is 0.
        :param y: The y-coordinate of the text box. Default is 0.
        :param width: The width of the text box. Default is 200.
        :param height: The height of the text box. Default is 30.
        :param placeholder: Placeholder text for the text box. Default is "Enter text...".
        """
        super().__init__(x, y, width, height)
        self._text = ""
        self._placeholder = placeholder

    @log_event
    def render(self, renderer: Renderer) -> None:
        """
        Render the text box using the provided renderer.

        :param renderer: The renderer responsible for drawing the text box.
        """
        renderer.render_textbox(self)

    @log_event
    def handle_event(self, event: Event) -> None:
        """
        Handle events for the text box.

        :param event: The event to handle.
        """
        if event.is_type(EventType.KEY_PRESS):
            key = event.get_data(str)
            if key:
                self._text += key

    @property
    def text(self) -> str:
        """Gets the current text in the text box."""
        return self._text

    @property
    def placeholder(self) -> str:
        """Gets the placeholder text of the text box."""
        return self._placeholder
