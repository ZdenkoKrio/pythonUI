from .custom_modifier import CustomModifier
from .styling import CombinedStylingModifier
from .animation import CombinedAnimationModifier


class Modifiers(CustomModifier, CombinedStylingModifier, CombinedAnimationModifier):
    """
    Combined mixin that integrates modifiers and styling functionality.
    """

    def __init__(self):
        CustomModifier.__init__(self)
        CombinedStylingModifier.__init__(self)
        CombinedAnimationModifier.__init__(self)
