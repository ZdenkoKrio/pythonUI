class TransformModifier:
    """
    Modifier for transformation properties such as rotation and scaling.
    """

    def __init__(self):
        self._rotation: float = 0.0  # Degrees
        self._scale_x: float = 1.0
        self._scale_y: float = 1.0

    def set_rotation(self, degrees: float) -> 'View':
        """
        Sets the rotation of the component.

        :param degrees: Rotation in degrees.
        :return: Self for chaining.
        """
        self._rotation = degrees
        return self

    def set_scale(self, scale_x: float, scale_y: float) -> 'View':
        """
        Sets the scaling of the component.

        :param scale_x: Horizontal scale factor.
        :param scale_y: Vertical scale factor.
        :return: Self for chaining.
        """
        self._scale_x = scale_x
        self._scale_y = scale_y
        return self
