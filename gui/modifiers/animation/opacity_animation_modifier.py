from .base_animation_manager import BaseAnimationManager
from .animation import Animation
from ..enums.animation_trigger import AnimationTrigger


class OpacityAnimationModifier(BaseAnimationManager):
    """
    Modifier for animating the opacity of a component.
    """

    def animate_opacity(self, opacity: float, duration: float, trigger: AnimationTrigger) -> 'View':
        """
        Adds an opacity animation to the component.

        :param opacity: Target opacity (0.0 to 1.0).
        :param duration: Animation duration in seconds.
        :param trigger: The trigger for when the animation should be played.
        :return: Self for chaining.
        """
        if not (0.0 <= opacity <= 1.0):
            raise ValueError("Opacity must be between 0.0 and 1.0.")
        animation = Animation(trigger, "opacity", {"opacity": opacity}, duration)
        self.add_animation(animation)
        return self
