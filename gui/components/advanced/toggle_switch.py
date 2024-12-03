from ...core import View, Renderer, Event, EventType
from ..interactive_component import InteractiveComponent
from ...utils import log_event, Observable


class Toggle(View[bool], InteractiveComponent, Observable):
    """
    A toggle switch component for binary selection.
    """

    def __init__(
        self,
        x: int,
        y: int,
        width: int = 50,
        height: int = 25,
        toggled: bool = False,
    ):
        """
        Initializes a toggle component.

        :param x: The x-coordinate of the toggle.
        :param y: The y-coordinate of the toggle.
        :param width: The width of the toggle. Default is 50.
        :param height: The height of the toggle. Default is 25.
        :param toggled: The initial state of the toggle. Default is False.
        """
        View.__init__(self, x, y, width, height)
        Observable.__init__(self)
        self.state = toggled  # Current toggled state

    @log_event
    def render(self, renderer: Renderer) -> None:
        """
        Renders the toggle.

        :param renderer: The renderer responsible for drawing the toggle.
        """
        self.apply_modifiers()
        renderer.render_toggle(self)

    def handle_event(self, event: Event) -> None:
        """
        Handles click events for the toggle.

        :param event: The event to handle.
        """
        if event.is_type(EventType.CLICK):
            self.state = not self.state
            self.notify_observers(state=self.state)

    def set_toggled(self, toggled: bool) -> 'Toggle':
        """
        Sets the toggled state.

        :param toggled: The new toggled state.
        :return: Self for chaining.
        """
        self.state = toggled
        return self
