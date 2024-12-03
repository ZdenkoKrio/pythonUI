from abc import ABC, abstractmethod
from ..core import View, Renderer
from typing import List


class Layout(View[None], ABC):
    """
    Abstract base class for layouts managing child components.
    """

    def __init__(self, x: int, y: int, width: int, height: int):
        """
        Initializes a layout.

        :param x: The x-coordinate of the layout.
        :param y: The y-coordinate of the layout.
        :param width: The width of the layout.
        :param height: The height of the layout.
        """
        super().__init__(x, y, width, height)
        self._components: List[View] = []

    def add_component(self, component: View) -> 'Layout':
        """
        Adds a component to the layout.

        :param component: The component to add.
        :return: Self for chaining.
        """
        self._components.append(component)
        return self

    def remove_component(self, component: View) -> 'Layout':
        """
        Removes a component from the layout.

        :param component: The component to remove.
        :return: Self for chaining.
        """
        if component in self._components:
            self._components.remove(component)
        return self

    @abstractmethod
    def arrange(self) -> None:
        """
        Arranges the components within the layout.
        Must be implemented by subclasses.
        """
        pass

    def render(self, renderer: Renderer) -> None:
        """
        Renders the layout and its components.

        :param renderer: The renderer responsible for drawing the layout.
        """
        self.apply_modifiers()
        for component in self._components:
            component.render(renderer)
