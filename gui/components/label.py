from core.view import View
from core.renderer import Renderer
from utils.logging import log_event
from utils.rendering.styles import Style


class Label(View):
    """
    Represents a label component with default parameters and styling support.
    """

    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        width: int = 200,
        height: int = 30,
        text: str = "Label",
        alignment: str = "left",  # Options: "left", "center", "right"
        style: Style = Style(),
    ):
        """
        Initializes a label component with default parameters.

        :param x: The x-coordinate of the label. Default is 0.
        :param y: The y-coordinate of the label. Default is 0.
        :param width: The width of the label. Default is 200.
        :param height: The height of the label. Default is 30.
        :param text: The text of the label. Default is "Label".
        :param alignment: The alignment of the text. Default is "left".
        :param style: Style object defining text appearance. Default is Style().
        """
        super().__init__(x, y, width, height)
        self._text = text
        self._alignment = alignment
        self._style = style

        if alignment not in {"left", "center", "right"}:
            raise ValueError("Alignment must be 'left', 'center', or 'right'.")

    @log_event
    def render(self, renderer: Renderer) -> None:
        """
        Render the label using the provided renderer.

        :param renderer: The renderer responsible for drawing the label.
        """
        renderer.render_label(
            text=self._text,
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.height,
            style=self._style,
            alignment=self._alignment,
        )

    @property
    def text(self) -> str:
        """Gets the text of the label."""
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        """Sets the text of the label."""
        self._text = value

    @property
    def alignment(self) -> str:
        """Gets the text alignment."""
        return self._alignment

    @property
    def style(self) -> Style:
        """Gets the style of the label."""
        return self._style
    