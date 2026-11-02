from src.simulation.value_generator import generator_batteryTemperature
from src.producers.event import build_event

SENSOR_ID = "sensor-temperature-battery-08"
SENSOR_TYPE = "temperature-battery"

def sensor_temperature_battery(batch_id, ramp_rate, seconds_elapsed, frozen_ref, drift_ref):
    value = generator_batteryTemperature(ramp_rate, seconds_elapsed, frozen_ref=frozen_ref, drift_ref=drift_ref)
    
    return build_event(SENSOR_ID, SENSOR_TYPE, batch_id, value)