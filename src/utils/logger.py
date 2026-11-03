import logging
import os
from logging.handlers import RotatingFileHandler

_configured = False

def get_logger(name: str) -> logging.Logger:
    _configure_root()
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger

def _configure_root() -> None:
    global _configured
    if _configured:
        return

    formatter = logging.Formatter('[%(asctime)s] - %(levelname)s - %(message)s')
    os.makedirs('logs', exist_ok=True)

    root = logging.getLogger()
    for handler in (
        logging.StreamHandler(),
        RotatingFileHandler('logs/pipeline.log', maxBytes=5_000_000, backupCount=3),
    ):
        handler.setFormatter(formatter)
        root.addHandler(handler)

    _configured = True