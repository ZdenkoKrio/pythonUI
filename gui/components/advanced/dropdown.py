from ...core import View, Renderer, Event, EventType
from ..interactive_component import InteractiveComponent
from ..label import Label
from ...utils import log_event, Observable
from typing import List, Optional


class Dropdown(View[Optional[Label]], InteractiveComponent, Observable):
    """
    A dropdown component for selecting a single Label option from a list.
    """

    def __init__(
        self,
        x: int,
        y: int,
        width: int = 200,
        height: int = 30,
        options: List[Label] = None,
        selected: Optional[Label] = None,
    ):
        """
        Initializes a dropdown component.

        :param x: The x-coordinate of the dropdown.
        :param y: The y-coordinate of the dropdown.
        :param width: The width of the dropdown. Default is 200.
        :param height: The height of the dropdown. Default is 30.
        :param options: A list of Label options to select from.
        :param selected: The initially selected Label option.
        """
        View.__init__(self, x, y, width, height)
        Observable.__init__(self)
        self._options = options or []
        self.state = selected  # Currently selected option

    @log_event
    def render(self, renderer: Renderer) -> None:
        """
        Renders the dropdown and its options.

        :param renderer: The renderer responsible for drawing the dropdown.
        """
        self.apply_modifiers()
        renderer.render_dropdown(self)

        # Render the selected option, if any
        if self.state:
            self.state.render(renderer)

    def handle_event(self, event: Event) -> None:
        """
        Handles click events for the dropdown.

        :param event: The event to handle.
        """
        if event.is_type(EventType.CLICK):
            selected_option = event.data.get("option", None)
            if selected_option in self._options:
                self.state = selected_option
                self.notify_observers(selected=self.state)

    def add_option(self, option: Label) -> 'Dropdown':
        """
        Adds a new Label option to the dropdown.

        :param option: The Label option to add.
        :return: Self for chaining.
        """
        if option not in self._options:
            self._options.append(option)
        return self

    def remove_option(self, option: Label) -> 'Dropdown':
        """
        Removes a Label option from the dropdown.

        :param option: The Label option to remove.
        :return: Self for chaining.
        """
        if option in self._options:
            self._options.remove(option)
        return self

    def set_selected(self, selected: Label) -> 'Dropdown':
        """
        Sets the selected Label option.

        :param selected: The Label option to select.
        :return: Self for chaining.
        """
        if selected in self._options:
            self.state = selected
        return self

    @property
    def options(self) -> List[Label]:
        """
        Gets the list of available Label options.
        """
        return self._options
