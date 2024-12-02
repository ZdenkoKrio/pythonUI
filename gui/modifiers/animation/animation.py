from typing import Dict
from ..enums.animation_trigger import AnimationTrigger


class Animation:
    """
    Represents an animation with its properties.
    """

    def __init__(self, trigger: AnimationTrigger, animation_type: str, target_values: Dict, duration: float):
        """
        Initializes an animation.

        :param trigger: The trigger for the animation.
        :param animation_type: The type of animation (e.g., "position", "size", "opacity").
        :param target_values: The target values for the animation.
        :param duration: The duration of the animation in seconds.
        """
        if duration <= 0:
            raise ValueError("Duration must be greater than 0.")

        self.trigger: AnimationTrigger = trigger
        self.animation_type: str = animation_type
        self.target_values: Dict = target_values
        self.duration: float = duration

    def __repr__(self) -> str:
        """
        String representation of the animation.
        """
        return (
            f"Animation(trigger={self.trigger}, "
            f"type={self.animation_type}, "
            f"targets={self.target_values}, "
            f"duration={self.duration}s)"
        )
