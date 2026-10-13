import json
from utils.decorators import log_kinesis_end 

@log_kinesis_end
def send_kinesis(client, stream_name, record, partition_key):
    return client.put_record(
            StreamName=stream_name,
            Data=json.dumps(record),
            PartitionKey=partition_key
        )