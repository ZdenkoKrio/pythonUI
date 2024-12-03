from ..core import View, Renderer, Event, EventType
from .interactive_component import InteractiveComponent
from .label import Label
from typing import Optional, Callable
from ..utils import log_event


class Button(View[bool], InteractiveComponent):
    """
    A button component with a text label and click functionality.
    """

    def __init__(
        self,
        x: int,
        y: int,
        width: int = 100,
        height: int = 50,
        text: str = "Button",
        callback: Optional[Callable[[], None]] = None,
    ):
        """
        Initializes a button component.

        :param x: The x-coordinate of the button.
        :param y: The y-coordinate of the button.
        :param width: The width of the button. Default is 100.
        :param height: The height of the button. Default is 50.
        :param text: The text of the button.
        :param callback: A callable function to execute on button click.
        """
        super().__init__(x, y, width, height)
        self.state = False  # Button's default state (not clicked)
        self.text_label = Label(0, 0, width, height, text)  # Inner label for text
        self._callback = callback

    @log_event
    def render(self, renderer: Renderer) -> None:
        """
        Renders the button and its inner text label.

        :param renderer: The renderer responsible for drawing the button.
        """
        self.apply_modifiers()  # Apply all modifiers to the button
        renderer.render_button(self)  # Render the button itself
        self.text_label.render(renderer)  # Render the inner label for text

    def handle_event(self, event: Event) -> None:
        """
        Handles click events for the button.

        :param event: The event to handle.
        """
        if event.is_type(EventType.CLICK):
            self.state = True
            if self._callback:
                self._callback()
            self.state = False  # Reset state after the callback

    def set_text(self, text: str) -> 'Button':
        """
        Sets the text of the button.

        :param text: The new text value.
        :return: Self for chaining.
        """
        self.text_label.set_text(text)
        return self
