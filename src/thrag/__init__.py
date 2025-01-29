import sys
import time

import structlog


def configure_logging():
    # You can customize processors, e.g., JSON or console-friendly
    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.stdlib.BoundLogger,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

logger = structlog.get_logger("thrag")

def time_function(func):
    """
    Decorator to measure execution time.
    Logs as debug with the function name and elapsed time.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        logger.debug("timing", function=func.__name__, seconds=elapsed)
        return result
    return wrapper