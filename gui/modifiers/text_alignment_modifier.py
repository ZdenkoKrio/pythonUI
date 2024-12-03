from enums.text_alignment import TextAlignment


class TextAlignmentModifier:
    """
    Modifier for text alignment.
    """

    def __init__(self):
        self._text_alignment: TextAlignment = TextAlignment.LEFT

    def set_text_alignment(self, alignment: TextAlignment) -> 'View':
        """
        Sets the text alignment for the component.

        :param alignment: The desired text alignment (LEFT, CENTER, RIGHT).
        :return: Self for chaining.
        """
        if not isinstance(alignment, TextAlignment):
            raise ValueError("Alignment must be a valid TextAlignment enum value.")
        self._text_alignment = alignment
        return self

    @property
    def text_alignment(self) -> TextAlignment:
        """
        Gets the current text alignment.

        :return: The current text alignment.
        """
        return self._text_alignment
