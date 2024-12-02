from typing import List
from .animation import Animation
from ..enums.animation_trigger import AnimationTrigger


class BaseAnimationManager:
    """
    Base class for managing animations in components.
    """

    def __init__(self):
        # Store animations as a list of Animation objects
        self._animations: List[Animation] = []

    def add_animation(self, animation: Animation) -> None:
        """
        Adds an animation to the manager.

        :param animation: An instance of the Animation class.
        """
        self._animations.append(animation)

    def play_animations(self, trigger: AnimationTrigger) -> None:
        """
        Plays animations associated with a specific trigger.

        :param trigger: The trigger for which animations should be played.
        """
        for animation in self._animations:
            if animation.trigger == trigger:
                print(f"Playing {animation}")

    def clear_animations(self) -> None:
        """
        Clears all animations from the manager.
        """
        self._animations = []
