import hashlib
import json
from src.simulation.value_generator import generator_batteryTemperature
from datetime import datetime, timezone

def sensor_temperature_battery(id, degradation, frozen_ref):
    timestamp = datetime.now(timezone.utc).isoformat()
    value = generator_batteryTemperature(degradation=degradation, frozen_ref=frozen_ref)
    
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
        "sensor_id": "sensor-temperature-battery-08",
        "type": "temperature-battery",
        "value": value,
        "event_timestamp": timestamp
    }