from ...core import View, Renderer, Event, EventType
from ..interactive_component import InteractiveComponent
from ...utils import log_event, Observable


class Checkbox(View[bool], InteractiveComponent, Observable):
    """
    A checkbox component for binary selection with observable state.
    """

    def __init__(
        self,
        x: int,
        y: int,
        size: int = 20,
        checked: bool = False,
        value: str = "",
    ):
        """
        Initializes a checkbox component.

        :param x: The x-coordinate of the checkbox.
        :param y: The y-coordinate of the checkbox.
        :param size: The size of the checkbox. Default is 20.
        :param checked: The initial state of the checkbox. Default is False.
        :param value: The value associated with this checkbox.
        """
        View.__init__(self, x, y, size, size)
        Observable.__init__(self)
        self.state = checked
        self._value = value

    @log_event
    def render(self, renderer: Renderer) -> None:
        """
        Renders the checkbox.

        :param renderer: The renderer responsible for drawing the checkbox.
        """
        self.apply_modifiers()
        renderer.render_checkbox(self)

    def handle_event(self, event: Event) -> None:
        """
        Handles click events for the checkbox.

        :param event: The event to handle.
        """
        if event.is_type(EventType.CLICK):
            self.state = not self.state
            self.notify_observers(state=self.state, value=self._value)

    @property
    def value(self) -> str:
        """Gets the value associated with the checkbox."""
        return self._value
