from layout import Layout


class GridStack(Layout):
    """
    A layout that arranges components in a grid.
    """

    def __init__(self, x: int, y: int, width: int, height: int, rows: int, cols: int):
        """
        Initializes a grid stack.

        :param x: The x-coordinate of the grid stack.
        :param y: The y-coordinate of the grid stack.
        :param width: The width of the grid stack.
        :param height: The height of the grid stack.
        :param rows: Number of rows in the grid.
        :param cols: Number of columns in the grid.
        """
        super().__init__(x, y, width, height)
        self._rows = rows
        self._cols = cols

    def arrange(self) -> None:
        """
        Arranges components in a grid within the layout.
        """
        if not self._components:
            return

        cell_width = self.width // self._cols
        cell_height = self.height // self._rows

        for index, component in enumerate(self._components):
            row = index // self._cols
            col = index % self._cols

            component.x = self.x + col * cell_width
            component.y = self.y + row * cell_height
            component.width = cell_width
            component.height = cell_height
