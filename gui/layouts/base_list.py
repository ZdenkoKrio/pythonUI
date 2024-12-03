from abc import ABC, abstractmethod
from ..core import View, Renderer
from typing import List


class BaseList(View[None], ABC):
    """
    Abstract base class for lists.
    """

    def __init__(self, x: int, y: int, width: int, height: int, item_size: int):
        """
        Initializes the base list.

        :param x: The x-coordinate of the list.
        :param y: The y-coordinate of the list.
        :param width: The width of the list.
        :param height: The height of the list.
        :param item_size: The size of each item in the list (width for horizontal, height for vertical).
        """
        super().__init__(x, y, width, height)
        self._item_size = item_size
        self._items: List[View] = []

    def add_item(self, item: View) -> 'BaseList':
        """
        Adds an item to the list.

        :param item: The item to add.
        :return: Self for chaining.
        """
        self._items.append(item)
        self.arrange_items()
        return self

    @abstractmethod
    def arrange_items(self) -> None:
        """
        Arranges items in the list.
        Must be implemented by subclasses.
        """
        pass

    def render(self, renderer: Renderer) -> None:
        """
        Renders the list and its items.

        :param renderer: The renderer responsible for drawing the list.
        """
        self.apply_modifiers()
        for item in self._items:
            item.render(renderer)
