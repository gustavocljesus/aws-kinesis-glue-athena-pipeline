import json
import logging
from botocore.exceptions import BotoCoreError, ClientError

logger = logging.getLogger(__name__)

def envia_kinesis(cliente, stream_name, registro, partition_key):
    try:
        return cliente.put_record(
        StreamName = stream_name,
        Data = json.dumps(registro),
        PartitionKey = partition_key
        )
    except (BotoCoreError, ClientError) as e:
         logger.error(f"Erro ao enviar para o Kinesis: {e}")
         return None
        