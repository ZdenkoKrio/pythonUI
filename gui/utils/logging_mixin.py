import logging


class LoggingMixin:
    """
    Mixin that logs all method calls of a class.
    """

    def __getattribute__(self, name):
        attr = super().__getattribute__(name)
        if callable(attr):
            def logged_method(*args, **kwargs):
                logging.info(f"Method {name} called with args: {args}, kwargs: {kwargs}")
                result = attr(*args, **kwargs)
                logging.info(f"Method {name} returned {result}")
                return result
            return logged_method
        return attr
