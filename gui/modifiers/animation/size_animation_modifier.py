from .base_animation_manager import BaseAnimationManager
from .animation import Animation
from ..enums.animation_trigger import AnimationTrigger


class SizeAnimationModifier(BaseAnimationManager):
    """
    Modifier for animating the size of a component.
    """

    def animate_size(self, width: int, height: int, duration: float, trigger: AnimationTrigger) -> 'View':
        """
        Adds a size animation to the component.

        :param width: Target width.
        :param height: Target height.
        :param duration: Animation duration in seconds.
        :param trigger: The trigger for when the animation should be played.
        :return: Self for chaining.
        """
        animation = Animation(trigger, "size", {"width": width, "height": height}, duration)
        self.add_animation(animation)
        return self
