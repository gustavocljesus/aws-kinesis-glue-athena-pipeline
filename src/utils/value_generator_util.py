from random import uniform
from chance_error_util import apply_error, maybe_outlier

def generator_hydraulicPressure(error_rate=0.1, degradation=False):
    if degradation:
        error_rate = min(error_rate * 3, 1.0)

    value = maybe_outlier(
        normal_fn=lambda: round(uniform(150, 180), 4),
        outlier_fn=lambda: round(uniform(180, 200), 4)
    )
    return apply_error(value, error_rate)

def generator_batteryTemperature(error_rate=0.1, degradation=False):
    if degradation:
        error_rate = min(error_rate * 3, 1.0)

    value = maybe_outlier(
        normal_fn=lambda: round(uniform(20, 35), 4),
        outlier_fn=lambda: round(uniform(35, 45), 4)
    )
    return apply_error(value, error_rate)

def generator_powerFactor(error_rate=0.1, degradation=False):
    if degradation:
        error_rate = min(error_rate * 3, 1.0)

    value = maybe_outlier(
        normal_fn=lambda: round(uniform(0.92, 1.0), 4),
        outlier_fn=lambda: round(uniform(0.85, 0.92), 4)
    )
    return apply_error(value, error_rate)