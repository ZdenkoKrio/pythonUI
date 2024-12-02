from .base_animation_manager import BaseAnimationManager
from .animation import Animation
from ..enums.animation_trigger import AnimationTrigger


class PositionAnimationModifier(BaseAnimationManager):
    """
    Modifier for animating the position of a component.
    """

    def animate_position(self, x: int, y: int, duration: float, trigger: AnimationTrigger) -> 'View':
        """
        Adds a position animation to the component.

        :param x: Target x-coordinate.
        :param y: Target y-coordinate.
        :param duration: Animation duration in seconds.
        :param trigger: The trigger for when the animation should be played.
        :return: Self for chaining.
        """
        animation = Animation(trigger, "position", {"x": x, "y": y}, duration)
        self.add_animation(animation)
        return self
