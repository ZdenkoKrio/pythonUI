from ...core import View, Renderer
from ...utils import log_event


class ProgressBar(View[int]):
    """
    A progress bar component for visualizing progress.
    """

    def __init__(self, x: int, y: int, width: int = 300, height: int = 20, progress: int = 0):
        """
        Initializes a progress bar component.

        :param x: The x-coordinate of the progress bar.
        :param y: The y-coordinate of the progress bar.
        :param width: The width of the progress bar. Default is 300.
        :param height: The height of the progress bar. Default is 20.
        :param progress: The initial progress percentage (0-100). Default is 0.
        """
        super().__init__(x, y, width, height)
        self.state = max(0, min(100, progress))  # Ensure progress is between 0 and 100

    @log_event
    def render(self, renderer: Renderer) -> None:
        """
        Renders the progress bar.

        :param renderer: The renderer responsible for drawing the progress bar.
        """
        self.apply_modifiers()
        renderer.render_progressbar(self)

    def set_progress(self, progress: int) -> 'ProgressBar':
        """
        Sets the progress value.

        :param progress: The new progress value (0-100).
        :return: Self for chaining.
        """
        self.state = max(0, min(100, progress))
        return self
