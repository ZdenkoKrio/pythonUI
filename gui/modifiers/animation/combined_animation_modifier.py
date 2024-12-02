from .position_animation_modifier import PositionAnimationModifier
from .size_animation_modifier import SizeAnimationModifier
from .opacity_animation_modifier import OpacityAnimationModifier


class CombinedAnimationModifier(PositionAnimationModifier, SizeAnimationModifier, OpacityAnimationModifier):
    """
    Combined modifier for integrating all animation-related functionalities.
    """

    def __init__(self):
        PositionAnimationModifier.__init__(self)
        SizeAnimationModifier.__init__(self)
        OpacityAnimationModifier.__init__(self)
