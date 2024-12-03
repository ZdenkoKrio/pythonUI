from ...core import View, Renderer, Event, EventType
from ..interactive_component import InteractiveComponent
from ...utils import log_event, Observable
from typing import Optional


class RadioButton(View[bool], InteractiveComponent, Observable):
    """
    A radio button component for selecting a single option in a group.
    """

    def __init__(
        self,
        x: int,
        y: int,
        size: int = 20,
        value: str = "",
        group: Optional['RadioGroup'] = None,
    ):
        """
        Initializes a radio button component.

        :param x: The x-coordinate of the radio button.
        :param y: The y-coordinate of the radio button.
        :param size: The size of the radio button. Default is 20.
        :param value: The value associated with this radio button.
        :param group: The group this radio button belongs to.
        """
        View.__init__(self, x, y, size, size)
        Observable.__init__(self)
        self.state = False
        self._value = value
        self._group = group
        if group:
            group.add_button(self)

    @log_event
    def render(self, renderer: Renderer) -> None:
        """
        Renders the radio button.

        :param renderer: The renderer responsible for drawing the radio button.
        """
        self.apply_modifiers()
        renderer.render_radiobutton(self)

    def handle_event(self, event: Event) -> None:
        """
        Handles click events for the radio button.

        :param event: The event to handle.
        """
        if event.is_type(EventType.CLICK) and self._group:
            self._group.select(self)

    @property
    def value(self) -> str:
        """Gets the value associated with the radio button."""
        return self._value
