from ...core import View, Renderer, Event, EventType
from ..interactive_component import InteractiveComponent
from ...utils import log_event


class Slider(View[int], InteractiveComponent):
    """
    A slider component for selecting a value in a range.
    """

    def __init__(
        self,
        x: int,
        y: int,
        width: int = 300,
        min_value: int = 0,
        max_value: int = 100,
        initial_value: int = 0,
    ):
        """
        Initializes a slider component.

        :param x: The x-coordinate of the slider.
        :param y: The y-coordinate of the slider.
        :param width: The width of the slider. Default is 300.
        :param min_value: The minimum value of the slider. Default is 0.
        :param max_value: The maximum value of the slider. Default is 100.
        :param initial_value: The initial value of the slider. Default is 0.
        """
        super().__init__(x, y, width, 20)  # Fixed height for sliders
        self._min_value = min_value
        self._max_value = max_value
        self.state = initial_value

    @log_event
    def render(self, renderer: Renderer) -> None:
        """
        Renders the slider.

        :param renderer: The renderer responsible for drawing the slider.
        """
        self.apply_modifiers()
        renderer.render_slider(self)

    def handle_event(self, event: Event) -> None:
        """
        Handles events for the slider.

        :param event: The event to handle.
        """
        if event.is_type(EventType.CLICK):
            position = event.data.get("position", 0)
            relative_position = max(0, min(self.width, position - self.x))
            self.state = self._min_value + int((relative_position / self.width) * (self._max_value - self._min_value))

    def set_value(self, value: int) -> 'Slider':
        """
        Sets the slider value.

        :param value: The new slider value.
        :return: Self for chaining.
        """
        if self._min_value <= value <= self._max_value:
            self.state = value
        return self
