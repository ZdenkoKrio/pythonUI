class ShadowModifier:
    """
    Modifier for shadow properties.
    """

    def __init__(self):
        self._shadow_offset_x: int = 0
        self._shadow_offset_y: int = 0
        self._shadow_blur: int = 0
        self._shadow_color: str = "#000000"

    def set_shadow(self, offset_x: int, offset_y: int, blur: int, color: str) -> 'View':
        """
        Sets the shadow properties.

        :param offset_x: Horizontal offset of the shadow.
        :param offset_y: Vertical offset of the shadow.
        :param blur: Blur radius of the shadow.
        :param color: Shadow color in HEX format.
        :return: Self for chaining.
        """
        self._shadow_offset_x = offset_x
        self._shadow_offset_y = offset_y
        self._shadow_blur = blur
        self._shadow_color = color
        return self
