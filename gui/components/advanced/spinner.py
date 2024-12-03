from ...core import View, Renderer
from ...utils import log_event


class Spinner(View[None]):
    """
    A spinner component for indicating loading.
    """

    def __init__(self, x: int, y: int, size: int = 50):
        super().__init__(x, y, size, size)

    @log_event
    def render(self, renderer: Renderer) -> None:
        """
        Renders the spinner.

        :param renderer: The renderer responsible for drawing the spinner.
        """
        self.apply_modifiers()
        renderer.render_spinner(self)
