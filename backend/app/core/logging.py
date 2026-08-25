import logging
import sys


def setup_logging():
    """Configure structured JSON-style production logging format."""
    log_format = (
        "%(asctime)s [%(levelname)s] %(name)s (%(filename)s:%(lineno)d): %(message)s"
    )
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    # Quiet verbose loggers
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
