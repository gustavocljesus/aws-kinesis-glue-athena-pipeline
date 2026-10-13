import time
import functools
from src.utils.logger import get_logger

logger = get_logger(__name__)

def log_kinesis_end(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        record = args[2]
        sensor = record.get("type", "unknown")
        batch_id = record.get("batch_id")
        start_time = time.time()

        try:
            result = func(*args, **kwargs)
        except Exception as e:
            elapsed = round(time.time() - start_time, 3)
            logger.error(f"[{sensor}] failed after {elapsed}s | BatchId: {batch_id} | {e}")
            raise

        elapsed = round(time.time() - start_time, 3)
        logger.info(f"[{sensor}] sent in {elapsed}s | ShardId: {result['ShardId']} | BatchId: {batch_id}")
        return result
    return wrapper