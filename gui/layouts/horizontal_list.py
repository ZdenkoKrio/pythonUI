from .horizontal_stack import HorizontalStack
from .base_list import BaseList


class HorizontalList(BaseList, HorizontalStack):
    """
    A list that arranges items horizontally.
    """

    def __init__(self, x: int, y: int, width: int, height: int, item_width: int):
        """
        Initializes a horizontal list.

        :param x: The x-coordinate of the list.
        :param y: The y-coordinate of the list.
        :param width: The width of the list.
        :param height: The height of the list.
        :param item_width: The width of each item in the list.
        """
        super().__init__(x, y, width, height, item_width)

    def arrange_items(self) -> None:
        """
        Arranges items horizontally.
        """
        x_offset = self.x
        for item in self._items:
            item.x = x_offset
            item.y = self.y
            item.width = self._item_size
            item.height = self.height
            x_offset += self._item_size
