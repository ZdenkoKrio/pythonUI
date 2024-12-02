"""
This package provides modifiers for customizing and extending the appearance and behavior of components in the GUI library.

Modifiers are conceptually equivalent to "mixins" in object-oriented programming. They are designed to augment the functionality
of components inheriting from `View`. In this library, we use the term "modifier" instead of "mixin" to emphasize their purpose
in modifying the visual style, animations, and transformations of components.

Modifiers allow:
- Dynamic customization of component styles (e.g., colors, borders, shadows).
- Application of transformations (e.g., rotations, scaling).
- Easy extension of component functionality by composing multiple modifiers.

The key idea is to separate style-related logic from the core functionality of components, ensuring a modular and clean architecture.

--------------------------------------------------------------------------
This module provides modifiers and related enums for customizing component styles and behaviors.

The enums are centralized here for easier import and usage both within and outside the library.

Recommendation: Prefer creating new modifiers as mixins rather than using lambdas to ensure modularity, reusability, and clarity.
"""


from .modifiers import Modifiers
from .enums import FontStyle, BorderStyle, AnimationTrigger
from .animation import BaseAnimationManager, Animation


__all__ = [
    "Modifiers",

    # Enums
    "FontStyle",
    "BorderStyle",
    "AnimationTrigger",

    # Animations
    "BaseAnimationManager",
    "Animation",
]