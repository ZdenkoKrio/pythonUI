from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional
from .renderer import Renderer
from .events import Event
from ..utils.logging_mixin import LoggingMixin

T = TypeVar("T")


class View(LoggingMixin, ABC, Generic[T]):
    """
    Abstract base class for all visual components.
    """

    def __init__(self, x: int, y: int, width: int, height: int):
        """
        Initializes the component with position and size.

        :param x: The x-coordinate of the component.
        :param y: The y-coordinate of the component.
        :param width: The width of the component.
        :param height: The height of the component.
        """
        self._x: int = x
        self._y: int = y
        self._width: int = width
        self._height: int = height
        self._visible: bool = True
        self._state: Optional[T] = None

    @property
    def x(self) -> int:
        """Gets the x-coordinate of the component."""
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        """Sets the x-coordinate of the component."""
        self._x = value

    @property
    def y(self) -> int:
        """Gets the y-coordinate of the component."""
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        """Sets the y-coordinate of the component."""
        self._y = value

    @property
    def width(self) -> int:
        """Gets the width of the component."""
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        """Sets the width of the component."""
        self._width = value

    @property
    def height(self) -> int:
        """Gets the height of the component."""
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        """Sets the height of the component."""
        self._height = value

    def is_visible(self) -> bool:
        """
        Checks if the component is currently visible.

        :return: True if the component is visible, False otherwise.
        """
        return self._visible

    def show(self) -> None:
        """
        Makes the component visible.
        """
        self._visible = True

    def hide(self) -> None:
        """
        Hides the component.
        """
        self._visible = False

    @property
    def state(self) -> Optional[T]:
        """Gets the state of the component."""
        return self._state

    @state.setter
    def state(self, value: Optional[T]) -> None:
        """Sets the state of the component."""
        self._state = value

    @abstractmethod
    def render(self, renderer: Renderer) -> None:
        """
        Renders the component using the provided renderer.

        :param renderer: The renderer responsible for drawing the component.
        """
        pass

    @abstractmethod
    def handle_event(self, event: Event) -> None:
        """
        Handles an incoming event.

        :param event: The event to handle.
        """
        pass
