from typing import List
from .view import View
from .renderer import Renderer
from .events import Event
from ..utils.logging_mixin import LoggingMixin


class Window(LoggingMixin):
    """
    Represents a GUI window containing multiple views.
    """

    def __init__(self, title: str, width: int, height: int):
        """
        Initializes the window.

        :param title: The title of the window.
        :param width: The width of the window.
        :param height: The height of the window.
        """
        self._title: str = title
        self._width: int = width
        self._height: int = height
        self._views: List[View] = []

    @property
    def title(self) -> str:
        """Gets the title of the window."""
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        """Sets the title of the window."""
        self._title = value

    @property
    def width(self) -> int:
        """Gets the width of the window."""
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        """Sets the width of the window."""
        self._width = value

    @property
    def height(self) -> int:
        """Gets the height of the window."""
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        """Sets the height of the window."""
        self._height = value

    @property
    def views(self) -> List[View]:
        """Gets the list of views in the window."""
        return self._views

    def add_view(self, view: View) -> None:
        """
        Adds a view to the window.

        :param view: The view to add.
        """
        self._views.append(view)

    def render(self, renderer: Renderer) -> None:
        """
        Renders all views in the window.

        :param renderer: The renderer used to draw the views.
        """
        for view in self._views:
            if view.is_visible():
                view.render(renderer)

    def handle_event(self, event: Event) -> None:
        """
        Delegates the event to all views.

        :param event: The event to handle.
        """
        for view in self._views:
            view.handle_event(event)
