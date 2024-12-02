from typing import Callable, List


class CustomModifier:
    """
    Mixin for managing and applying modifiers to a component.
    """

    def __init__(self):
        self._modifiers: List[Callable[[object], None]] = []

    def add_modifier(self, modifier: Callable[['View'], None]) -> 'View':
        """
        Adds a modifier to the component.

        :param modifier: A callable function that modifies the component.
        :return: Self for chaining.
        """
        self._modifiers.append(modifier)
        return self

    def apply_modifiers(self) -> None:
        """
        Applies all modifiers to the component.
        """
        for modifier in self._modifiers:
            modifier(self)
