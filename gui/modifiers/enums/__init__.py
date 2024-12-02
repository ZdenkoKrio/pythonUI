"""
This module centralizes all Enum definitions used across the library.

Enums provide a consistent and type-safe way to define standard values such as styles, behaviors, and configurations.
"""

from .font_style import FontStyle
from .border_style import BorderStyle
from .animation_trigger import AnimationTrigger

__all__ = [
    "FontStyle",
    "BorderStyle",
    "AnimationTrigger",
]