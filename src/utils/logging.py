import logging
from logging.handlers import RotatingFileHandler
import os

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        os.makedirs('logs', exist_ok=True)
        file_handler = RotatingFileHandler('logs/pipeline.log', maxBytes=5_000_000, backupCount=3)
        file_handler.setFormatter(formatter)

        logger.setLevel(logging.INFO)
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

    return logger