from enum import Enum
from typing import Any, Optional, Type, TypeVar
from datetime import datetime
from ..utils.logging import log_event

T = TypeVar("T")


class EventType(Enum):
    """
    Enum representing types of events.

    Attributes:
        CLICK: Event triggered by a mouse click.
        KEY_PRESS: Event triggered by a keyboard key press.
        MOUSE_MOVE: Event triggered by mouse movement.
    """
    CLICK = "click"
    KEY_PRESS = "key_press"
    MOUSE_MOVE = "mouse_move"

    @classmethod
    def add_custom_type(cls, name: str) -> "EventType":
        """
        Dynamically adds a custom event type.

        :param name: The name of the custom event type.
        :return: The new EventType instance.
        """
        value = name.lower()
        if value in cls._value2member_map_:
            raise ValueError(f"EventType '{name}' already exists.")
        new_type = cls(value)
        cls._value2member_map_[value] = new_type
        return new_type


class Event:
    """
    Class representing an event in the GUI system.

    Attributes:
        type (EventType): The type of the event.
        data (Any): Additional data associated with the event.
        timestamp (datetime): The time the event was created.
        source (Optional[Any]): The source component that triggered the event.
        bubble (bool): Indicates whether the event should propagate.
    """

    def __init__(self, event_type: EventType, data: Any = None, source: Optional[Any] = None, bubble: bool = False):
        """
        Initializes the event.

        :param event_type: The type of the event.
        :param data: Additional data related to the event.
        :param source: The component that triggered the event.
        :param bubble: Whether the event should propagate to parent components.
        """
        self._type: EventType = event_type
        self._data: Any = data
        self._timestamp: datetime = datetime.now()
        self._source: Optional[Any] = source
        self._bubble: bool = bubble
        self._stopped: bool = False

    @property
    def type(self) -> EventType:
        """
        Gets the type of the event.

        :return: The type of the event.
        """
        return self._type

    @property
    def data(self) -> Any:
        """
        Gets the additional data associated with the event.

        :return: The event's data.
        """
        return self._data

    @property
    def timestamp(self) -> datetime:
        """
        Gets the timestamp when the event was created.

        :return: The timestamp of the event.
        """
        return self._timestamp

    @property
    def source(self) -> Optional[Any]:
        """
        Gets the source component that triggered the event.

        :return: The source component, or None if not set.
        """
        return self._source

    @property
    def bubble(self) -> bool:
        """
        Checks if the event should propagate to parent components.

        :return: True if the event should bubble, False otherwise.
        """
        return self._bubble

    def is_type(self, event_type: EventType) -> bool:
        """
        Checks if the event is of a specific type.

        :param event_type: The type to check against.
        :return: True if the event type matches, False otherwise.
        """
        return self._type == event_type

    def get_data(self, data_type: Type[T]) -> Optional[T]:
        """
        Gets the event data if it matches the expected type.

        :param data_type: The expected type of the data.
        :return: The data if it matches the type, otherwise None.
        """
        if isinstance(self._data, data_type):
            return self._data
        return None

    def get_data_or_default(self, data_type: Type[T], default: T) -> T:
        """
        Gets the event data if it matches the expected type; otherwise, returns a default value.

        :param data_type: The expected type of the data.
        :param default: The default value to return if types do not match.
        :return: The data if it matches the type, otherwise the default value.
        """
        if isinstance(self._data, data_type):
            return self._data
        return default

    def stop_propagation(self) -> None:
        """
        Stops the event from propagating further.
        """
        self._stopped = True

    def is_stopped(self) -> bool:
        """
        Checks if the event propagation is stopped.

        :return: True if propagation is stopped, False otherwise.
        """
        return self._stopped

    @log_event
    def process(self):
        """
        Processes the event (example method to demonstrate logging).
        """
        print(f"Processing event of type {self.type}")
