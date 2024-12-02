"""
Utilities module for the GUI library.

This module includes:
- LoggingMixin for automatic method call logging.
- log_event decorator for selective method logging.
"""

from .logging_mixin import LoggingMixin
from .logging import log_event

__all__ = [
    "LoggingMixin",
    "log_event",
]