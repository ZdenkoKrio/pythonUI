from ..core import View, Renderer, Event, EventType
from .interactive_component import InteractiveComponent
from ..utils import log_event


class TextBox(View[str], InteractiveComponent):
    """
    A text box component for user input, managing text directly via state.
    """

    def __init__(
        self,
        x: int,
        y: int,
        width: int = 300,
        height: int = 50,
        text: str = "",
        placeholder: str = "Enter text...",
    ):
        """
        Initializes a text box component.

        :param x: The x-coordinate of the text box.
        :param y: The y-coordinate of the text box.
        :param width: The width of the text box. Default is 300.
        :param height: The height of the text box. Default is 50.
        :param text: The initial text of the text box. Default is an empty string.
        :param placeholder: Placeholder text when no input is provided.
        """
        super().__init__(x, y, width, height)
        self.state = text  # The current text value
        self._placeholder = placeholder

    @log_event
    def render(self, renderer: Renderer) -> None:
        """
        Renders the text box, displaying state or placeholder if state is empty.

        :param renderer: The renderer responsible for drawing the text box.
        """
        self.apply_modifiers()
        text_to_display = self.state or self._placeholder
        renderer.render_textbox(self, text_to_display)

    def handle_event(self, event: Event) -> None:
        """
        Handles events for the text box.

        :param event: The event to handle.
        """
        if event.is_type(EventType.KEY_PRESS):
            key = event.data.get("key", "")
            if key == "BACKSPACE" and self.state:
                self.state = self.state[:-1]  # Remove last character
            elif len(key) == 1:  # Only process single character inputs
                self.state += key

    @property
    def placeholder(self) -> str:
        """Gets the placeholder text."""
        return self._placeholder

    @placeholder.setter
    def placeholder(self, value: str) -> None:
        """Sets a new placeholder text."""
        self._placeholder = value
