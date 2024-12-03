from ...core import View, Renderer
from ...utils import log_event


class Tooltip(View[str]):
    """
    A tooltip component for displaying additional information.
    """

    def __init__(self, x: int, y: int, text: str, width: int = 150, height: int = 50):
        """
        Initializes a tooltip component.

        :param x: The x-coordinate of the tooltip.
        :param y: The y-coordinate of the tooltip.
        :param text: The text to display in the tooltip.
        :param width: The width of the tooltip.
        :param height: The height of the tooltip.
        """
        super().__init__(x, y, width, height)
        self.state = text
        self._visible = False  # Tooltip is hidden by default

    @log_event
    def render(self, renderer: Renderer) -> None:
        """
        Renders the tooltip if visible.

        :param renderer: The renderer responsible for drawing the tooltip.
        """
        if self._visible:
            renderer.render_tooltip(self)

    def show(self) -> None:
        """Makes the tooltip visible."""
        self._visible = True

    def hide(self) -> None:
        """Hides the tooltip."""
        self._visible = False

    def attach_to(self, component: View) -> None:
        """
        Attaches the tooltip to a component, positioning it near the component.

        :param component: The component to attach the tooltip to.
        """
        self.x = component.x + component.width + 10
        self.y = component.y
