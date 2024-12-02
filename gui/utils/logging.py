import logging
from functools import wraps
from typing import Callable

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def log_event(log_level=logging.INFO) -> Callable:
    """
    Decorator to log method calls and their arguments with a specified log level.

    :param log_level: The logging level to use (e.g., logging.INFO, logging.DEBUG).
    :return: The decorated function.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Log entering the function
            logging.log(log_level, f"Entering: {func.__module__}.{func.__qualname__} | Args: {args}, Kwargs: {kwargs}")
            try:
                result = func(*args, **kwargs)
                # Log exiting the function
                logging.log(log_level, f"Exiting: {func.__module__}.{func.__qualname__} | Result: {result}")
                return result
            except Exception as e:
                # Log exceptions at ERROR level
                logging.error(f"Error in {func.__module__}.{func.__qualname__}: {e}", exc_info=True)
                raise
        return wrapper
    return decorator
