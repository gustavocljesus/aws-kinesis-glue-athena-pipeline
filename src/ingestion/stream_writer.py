import json
from utils.logging import get_logger
from utils.decorators import log_kinesis_end 
from botocore.exceptions import BotoCoreError, ClientError

logger = get_logger(__name__)

@log_kinesis_end
def send_kinesis(client, stream_name, register, partition_key):
    try:
        response = client.put_record(
            StreamName=stream_name,
            Data=json.dumps(register),
            PartitionKey=partition_key
        )
        return register, response
    except (BotoCoreError, ClientError) as e:
         logger.error(f"Erro ao enviar para o Kinesis: {e}")
         return None