from ..enums.font_style import FontStyle


class BaseStylingModifier:
    """
    Modifier for basic styling properties such as colors and text.
    """

    def __init__(self):
        self._background_color: str = "#FFFFFF"
        self._text_color: str = "#000000"
        self._font_size: int = 14
        self._font_style: FontStyle = FontStyle.NORMAL

    def set_background_color(self, color: str) -> 'View':
        """
        Sets the background color of the component.

        :param color: Background color in HEX format.
        :return: Self for chaining.
        """
        self._background_color = color
        return self

    def set_text_color(self, color: str) -> 'View':
        """
        Sets the text color of the component.

        :param color: Text color in HEX format.
        :return: Self for chaining.
        """
        self._text_color = color
        return self

    def set_font_size(self, size: int) -> 'View':
        """
        Sets the font size of the text.

        :param size: Font size in points.
        :return: Self for chaining.
        """
        self._font_size = size
        return self

    def set_font_style(self, style: FontStyle) -> 'View':
        """
        Sets the font style of the text.

        :param style: FontStyle enum value.
        :return: Self for chaining.
        """
        if not isinstance(style, FontStyle):
            raise ValueError(f"Font style must be an instance of FontStyle enum, got {style}")
        self._font_style = style
        return self
