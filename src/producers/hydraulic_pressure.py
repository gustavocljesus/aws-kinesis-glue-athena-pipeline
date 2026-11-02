from src.simulation.value_generator import generator_hydraulicPressure
from src.producers.event import build_event

SENSOR_ID = "sensor-hydraulic-01"
SENSOR_TYPE = "hydraulic-pressure"

def sensor_hydraulic(batch_id, ramp_rate, seconds_elapsed, frozen_ref, drift_ref):
    value = generator_hydraulicPressure(ramp_rate, seconds_elapsed, frozen_ref=frozen_ref, drift_ref=drift_ref)

    return build_event(SENSOR_ID, SENSOR_TYPE, batch_id, value)