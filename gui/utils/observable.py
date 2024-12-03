from typing import Callable, List


class Observable:
    """
    Base class for objects that can be observed.
    """

    def __init__(self):
        self._observers: List[Callable] = []

    def add_observer(self, observer: Callable) -> None:
        """
        Registers a new observer.

        :param observer: The observer callback to register.
        """
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs) -> None:
        """
        Notifies all registered observers of a change.

        :param args: Positional arguments to pass to observers.
        :param kwargs: Keyword arguments to pass to observers.
        """
        for observer in self._observers:
            observer(*args, **kwargs)
