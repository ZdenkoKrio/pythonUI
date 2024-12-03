from layout import Layout


class VerticalStack(Layout):
    """
    A layout that arranges components vertically.
    """

    def arrange(self) -> None:
        """
        Arranges components vertically within the layout.
        """
        y_offset = self.y
        for component in self._components:
            component.x = self.x
            component.y = y_offset
            y_offset += component.height