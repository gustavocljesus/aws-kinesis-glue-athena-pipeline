import boto3
import time
import os
from src.utils.logger import get_logger
from dotenv import load_dotenv
from src.cli import parse_args
from src.producers import (
    hydraulic_pressure as hp,
    power_factor as pf,
    temperature_battery as tb
)
from src.simulation.error_model import (new_frozen_ref, new_drift_ref)
from src.ingestion.stream_writer import send_kinesis
from botocore.exceptions import BotoCoreError, ClientError
from botocore.config import Config

logger = get_logger(__name__)
load_dotenv()
args = parse_args()

client = boto3.client('kinesis', config=Config(
    retries={
        'max_attempts': 3,
        'mode': 'standard'
    },
    connect_timeout=5,
    read_timeout=5
))
STREAM_NAME = os.environ["STREAM_NAME"]

SENSORS = ("hydraulic", "battery", "power")

frozen_refs = {name: new_frozen_ref() for name in SENSORS}
drift_refs = {name: new_drift_ref() for name in SENSORS}

def send_batch(client, stream_name: str, records: list) -> tuple[int, int]: 
    success = 0
    failed = 0

    for record in records:
        partition_key = record.get("sensor_id", "default")
        try:
            send_kinesis(client, stream_name, record, partition_key)
            success += 1
        except (BotoCoreError, ClientError):
            failed += 1

    return success, failed


if __name__ == "__main__":
    PAUSE = args.sleep 
    RAMP_RATE = 0.2 / args.ramp_duration

    batch_id = 0
    sent_successfully = 0
    failed_to_send = 0 

    start_pipeline = time.time()

    try:
        while True:
            batch_id += 1
            seconds_elapsed = round(time.time() - start_pipeline, 3)
            records = [
                hp.sensor_hydraulic(batch_id, RAMP_RATE, seconds_elapsed, frozen_ref=frozen_refs["hydraulic"], drift_ref=drift_refs["hydraulic"]),
                pf.sensor_power_factor(batch_id, RAMP_RATE, seconds_elapsed, frozen_ref=frozen_refs["power"], drift_ref=drift_refs["power"]),
                tb.sensor_temperature_battery(batch_id, RAMP_RATE, seconds_elapsed, frozen_ref=frozen_refs["battery"], drift_ref=drift_refs["battery"])
            ]

            success, failed = send_batch(client, STREAM_NAME, records)
            sent_successfully += success
            failed_to_send += failed

            time.sleep(PAUSE)

    except KeyboardInterrupt:
        logger.info("Pipeline interrupted by user.")

    finally:
        end_pipeline = round(time.time() - start_pipeline, 3)
        logger.info(f"Pipeline finished. Total successful: {sent_successfully} | Total failed: {failed_to_send} | Total time: {end_pipeline}s")
