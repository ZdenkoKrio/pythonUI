from abc import ABC, abstractmethod
from ..core.events import Event


class InteractiveComponent(ABC):
    """
    Interface for components that handle user interactions.
    """

    @abstractmethod
    def handle_event(self, event: Event) -> None:
        """
        Handles an incoming event.
        Must be implemented by subclasses.
        """
        pass
