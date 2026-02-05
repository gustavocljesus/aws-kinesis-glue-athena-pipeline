import boto3
import time
from producer import hydraulic_prepressure as hp, power_factor as pf, temperature_battery as tb
from streaming.kinesis_writer import envia_kinesis

cliente = boto3.client('kinesis')
stream_name = ''
partition_key = '02'

inicio = time.time()
duracao = 5 * 60 # 5 minutos (em segundos)

id = 0

while time.time() - inicio < duracao:
    id += 1
    registros = [
        pf.gerador(id),
        tb.gerador(id),
        hp.gerador(id)
    ]

    for registro in registros:
        envia_kinesis(
            cliente,
            stream_name,
            registro,
            partition_key
        )
    
    time.sleep(10)