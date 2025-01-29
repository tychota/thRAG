import structlog
import logging

def configure_logging(log_level=logging.INFO):
    """
    Configure structlog
    """
    # 1. Configure structlog to wrap Python's standard logging
    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),       # add a timestamp
            structlog.stdlib.add_log_level,                    # include log level
            structlog.processors.JSONRenderer(sort_keys=True), # or console-friendly 
                                                               # if you don't want JSON
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

