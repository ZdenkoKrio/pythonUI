from .base_styling_modifier import BaseStylingModifier
from .border_modifier import BorderModifier
from .shadow_modifier import ShadowModifier
from .transform_modifier import TransformModifier


class CombinedStylingModifier(BaseStylingModifier, BorderModifier, ShadowModifier, TransformModifier):
    """
    Combined modifier for integrating all styling-related properties.
    """
    def __init__(self):
        BaseStylingModifier.__init__(self)
        BorderModifier.__init__(self)
        ShadowModifier.__init__(self)
        TransformModifier.__init__(self)
