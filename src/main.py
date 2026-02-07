import boto3
import time
from producer import hydraulic_prepressure as hp, power_factor as pf, temperature_battery as tb
from streaming.kinesis_writer import envia_kinesis
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

load_dotenv()

cliente = boto3.client('kinesis')
stream_name = os.getenv("STREAM_NAME")
partition_key = os.getenv("PARTITION_KEY")

inicio = time.time()
duracao = int(os.getenv("STREAM_DURACAO", 300))
pausa = int(os.getenv("SLEEP_STREAM", 10))

id = 0

while time.time() - inicio < duracao:
    id += 1
    registros = [
        pf.gerador(id),
        tb.gerador(id),
        hp.gerador(id)
    ]

    for registro in registros:
        resposta = envia_kinesis(
            cliente,
            stream_name,
            registro,
            partition_key
        )
        
        if resposta is None:
            time.sleep(2)
            
            resposta = envia_kinesis(
                cliente,
                stream_name,
                registro,
                partition_key
            )

            if resposta is None:
                logging.error("Falha definitiva ao enviar registro")

    time.sleep(pausa)