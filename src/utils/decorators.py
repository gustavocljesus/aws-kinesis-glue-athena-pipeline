import time
import functools
from utils.logging import get_logger

logger = get_logger(__name__)

def log_kinesis_end(func):
    @functools.wraps(func)
    def wrapper(client, stream_name, record, partition_key):
        sensor = record.get("type", "unknown")
        batch_id = record.get("batch_id")
        start_time = time.time()
        result = func(client, stream_name, record, partition_key)
        elapsed = round(time.time() - start_time, 3)

        if result[1]:
            logger.info(f"[{sensor}] enviado em {elapsed}s | ShardId: {result[1]['ShardId']} | BatchId: {batch_id}")
        else:
            logger.error(f"[{sensor}] falha após {elapsed}s")
        
        return result
    return wrapper