"""
This package provides functionality for handling animations in the GUI library.

The package includes:
- Modifiers for individual animation types, such as position, size, and opacity.
- A combined modifier for integrating all animation functionalities into a single class.
- The Animation class, which represents an animation object with properties like type, duration, and target values.
- The AnimationTrigger enum, which defines when animations should be played (e.g., on_show, on_hide).

Modules:
- position_modifier: Handles animations related to the position of a component.
- size_modifier: Handles animations related to the size of a component.
- opacity_modifier: Handles animations related to the opacity of a component.
- combined_animation_modifier: Combines all animation-related functionalities.
- base_animation_manager: Provides a base class for managing animations.
- animation: Defines the Animation class for representing animations.
"""

from .base_animation_manager import BaseAnimationManager
from .animation import Animation
from .combined_animation_modifier import CombinedAnimationModifier

__all__ = [
    "BaseAnimationManager",
    "Animation",
    "CombinedAnimationModifier",
]