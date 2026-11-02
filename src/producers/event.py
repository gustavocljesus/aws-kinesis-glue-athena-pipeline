import hashlib
import json
from datetime import datetime, timezone

def build_event(sensor_id: str, sensor_type: str, batch_id: int, value, timestamp: str | None = None) -> dict:
    timestamp = timestamp or datetime.now(timezone.utc).isoformat()

    event_id = hashlib.sha256(
        json.dumps({
            "sensor_id": sensor_id,
            "batch_id": batch_id,
            "value": value,
            "timestamp": timestamp
        }, sort_keys=True).encode()
    ).hexdigest()

    return {
        "event_id": event_id,
        "batch_id": batch_id,
        "sensor_id": sensor_id,
        "type": sensor_type,
        "value": value,
        "event_timestamp": timestamp
    }