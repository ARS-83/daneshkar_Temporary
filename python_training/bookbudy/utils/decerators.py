from functools import wraps
from logger import logger

def log_reading(func):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            book = args[0]
            logger.info(f"Reading '{book.title}' by {book.author}...")
            result = func(*args, **kwargs)
            logger.info(f"Reading session for '{book.title}' ended.")
            return result
        return wrapper
    return decorator