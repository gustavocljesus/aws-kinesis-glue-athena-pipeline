import hashlib
import json
from src.simulation.value_generator import generator_powerFactor
from datetime import datetime, timezone

def sensor_power_factor(id, degradation, frozen_ref):
    timestamp = datetime.now(timezone.utc).isoformat()
    value = generator_powerFactor(degradation=degradation, frozen_ref=frozen_ref)

    event_id = hashlib.sha256(
        json.dumps({
            "batch_id": id,
            "value": value,
            "timestamp": timestamp
        }, sort_keys=True).encode()
    ).hexdigest()

    return {
        "event_id": event_id,
        "batch_id": id,
        "sensor_id": "sensor-power-factor-05",
        "type": "power-factor",
        "value": value,
        "event_timestamp": timestamp
    }