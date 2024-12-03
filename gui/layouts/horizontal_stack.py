from layout import Layout


class HorizontalStack(Layout):
    """
    A layout that arranges components horizontally.
    """

    def arrange(self) -> None:
        """
        Arranges components horizontally within the layout.
        """
        x_offset = self.x
        for component in self._components:
            component.x = x_offset
            component.y = self.y
            x_offset += component.width
