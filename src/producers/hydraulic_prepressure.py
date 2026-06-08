import hashlib
import json
from src.utils.value_generator import generator_hydraulicPressure
from datetime import datetime, timezone

def sensor_hydraulic(id, degradation, frozen_ref):
    timestamp = datetime.now(timezone.utc).isoformat()
    value = generator_hydraulicPressure(degradation=degradation, frozen_ref=frozen_ref)

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
        "sensor_id": "sensor_hydraulic-01",
        "type": "hydraulic_pressure",
        "value": value,
        "event_timestamp": timestamp
    }

if __name__ == "__main__":
    print(sensor_hydraulic(id=1, degradation=True, frozen_ref={"value": 160.0}))