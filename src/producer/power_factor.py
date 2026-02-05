import boto3
import json
from random import uniform
from datetime import datetime, timezone
import time

cliente = boto3.client('kinesis')

duracao = 5 * 60 # 5 minutos (em segundos)
inicio = time.time()


while time.time() - inicio < duracao:
    dados = uniform(0.8, 1)
    id += 1
    
    registro = {'id': str(id), 
                'data': str(dados), 
                'type': 'power factor', 
                'timestamp': datetime.now(timezone.utc).isoformat()
                }
    
    cliente.put_record(
        StreamName = '', 
        Data = json.dumps(registro), 
        PartitionKey = '02'
        )

    time.sleep(10)
