from enum import Enum


class AnimationTrigger(Enum):
    """
    Enum representing animation triggers.
    """
    ON_SHOW = "on_show"
    ON_EVENT = "on_event"
    CONTINUOUS = "continuous"
    ON_HIDE = "on_hide"
