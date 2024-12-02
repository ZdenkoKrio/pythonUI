from ..enums.border_style import BorderStyle


class BorderModifier:
    """
    Modifier for border properties.
    """

    def __init__(self):
        self._border_width: int = 0
        self._border_color: str = "#000000"
        self._border_style: BorderStyle = BorderStyle.SOLID

    def set_border(self, width: int, color: str, style: BorderStyle) -> 'View':
        """
        Sets the border properties.

        :param width: Border width in pixels.
        :param color: Border color.
        :param style: BorderStyle enum value.
        :return: Self for chaining.
        """
        if not isinstance(style, BorderStyle):
            raise ValueError(f"Border style must be an instance of BorderStyle enum, got {style}")
        self._border_width = width
        self._border_color = color
        self._border_style = style
        return self
