from .vertical_stack import VerticalStack
from .base_list import BaseList


class VerticalList(BaseList, VerticalStack):
    """
    A list that arranges items vertically.
    """

    def __init__(self, x: int, y: int, width: int, height: int, item_height: int):
        """
        Initializes a vertical list.

        :param x: The x-coordinate of the list.
        :param y: The y-coordinate of the list.
        :param width: The width of the list.
        :param height: The height of the list.
        :param item_height: The height of each item in the list.
        """
        super().__init__(x, y, width, height, item_height)

    def arrange_items(self) -> None:
        """
        Arranges items vertically.
        """
        y_offset = self.y
        for item in self._items:
            item.x = self.x
            item.y = y_offset
            item.width = self.width
            item.height = self._item_size
            y_offset += self._item_size
