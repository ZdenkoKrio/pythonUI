from ..core.view import View
from ..core.renderer import Renderer
from ..core.events import Event, EventType
from ..utils.logging import log_event
from typing import Optional


class Button(View):
    """
    Represents a button component with default parameters.
    """

    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        width: int = 100,
        height: int = 50,
        label: str = "Button",
        callback: Optional[callable] = None,
    ):
        """
        Initializes a button component with default parameters.

        :param x: The x-coordinate of the button. Default is 0.
        :param y: The y-coordinate of the button. Default is 0.
        :param width: The width of the button. Default is 100.
        :param height: The height of the button. Default is 50.
        :param label: The text label of the button. Default is "Button".
        :param callback: A callable function to execute on button click. Default is None.
        """
        super().__init__(x, y, width, height)
        self._label = label
        self._callback = callback

    @log_event
    def render(self, renderer: Renderer) -> None:
        """
        Render the button using the provided renderer.

        :param renderer: The renderer responsible for drawing the button.
        """
        renderer.render_button(self)

    @log_event
    def handle_event(self, event: Event) -> None:
        """
        Handle events for the button.

        :param event: The event to handle.
        """
        if event.is_type(EventType.CLICK) and self._callback:
            self._callback()

    @property
    def label(self) -> str:
        """Gets the label of the button."""
        return self._label
