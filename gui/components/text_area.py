from .textbox import TextBox


class TextArea(TextBox):
    """
    A text area component for multi-line user input.
    """

    def __init__(
        self,
        x: int,
        y: int,
        width: int = 300,
        height: int = 150,
        text: str = "",
        placeholder: str = "Enter text...",
    ):
        """
        Initializes a text area component.

        :param x: The x-coordinate of the text area.
        :param y: The y-coordinate of the text area.
        :param width: The width of the text area. Default is 300.
        :param height: The height of the text area. Default is 150.
        :param text: The initial text of the text area. Default is an empty string.
        :param placeholder: Placeholder text when no input is provided.
        """
        super().__init__(x, y, width, height, text, placeholder)
