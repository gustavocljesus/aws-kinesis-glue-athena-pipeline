import json

def envia_kinesis(cliente, stream_name, registro, partition_key):
    return cliente.put_record(
        StreamName = stream_name,
        Data = json.dumps(registro),
        PartitionKey = partition_key
    )