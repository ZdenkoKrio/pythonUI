from ..core import Renderer, View
from typing import List, Optional
from ..utils import log_event


class Card(View[None]):
    """
    A card component for grouping other components.
    """

    def __init__(
        self,
        x: int,
        y: int,
        width: int = 400,
        height: int = 300,
        children: Optional[List[View]] = None,
    ):
        """
        Initializes a card component.

        :param x: The x-coordinate of the card.
        :param y: The y-coordinate of the card.
        :param width: The width of the card. Default is 400.
        :param height: The height of the card. Default is 300.
        :param children: A list of child components to render inside the card.
        """
        super().__init__(x, y, width, height)
        self._children = children or []

    @log_event
    def render(self, renderer: Renderer) -> None:
        """
        Renders the card and its child components.

        :param renderer: The renderer responsible for drawing the card.
        """
        self.apply_modifiers()
        renderer.render_card(self)
        for child in self._children:
            child.render(renderer)

    def add_child(self, child: View) -> 'Card':
        """
        Adds a child component to the card.

        :param child: The child component to add.
        :return: Self for chaining.
        """
        self._children.append(child)
        return self
