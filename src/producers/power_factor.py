from src.simulation.value_generator import generator_powerFactor
from src.producers.event import build_event

SENSOR_ID = "sensor-power-factor-05"
SENSOR_TYPE = "power-factor"

def sensor_power_factor(batch_id, ramp_rate, seconds_elapsed, frozen_ref, drift_ref):
    value = generator_powerFactor(ramp_rate, seconds_elapsed, frozen_ref=frozen_ref, drift_ref=drift_ref)

    return build_event(SENSOR_ID, SENSOR_TYPE, batch_id, value)