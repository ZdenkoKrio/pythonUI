from layout import Layout


class ZStack(Layout):
    """
    A layout that stacks components on top of each other.
    """

    def arrange(self) -> None:
        """
        Arranges components in a stacked manner, overlapping each other.
        """
        for component in self._components:
            component.x = self.x
            component.y = self.y
