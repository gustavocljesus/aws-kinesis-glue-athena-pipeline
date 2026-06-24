from random import uniform
from .error_model import apply_error, maybe_outlier

def generator_hydraulicPressure(error_rate=0.1, degradation=False, frozen_ref=None):
    if degradation:
        error_rate = min(error_rate * 3, 1.0)

    value = maybe_outlier(
        normal_fn=lambda: round(uniform(150, 180), 4),
        outlier_fn=lambda: round(uniform(180, 200), 4)
    )
    return apply_error(value, error_rate,
        error_weights={'missing': 0.40, 'frozen': 0.30, 'bias': 0.20, 'drift': 0.10},
        frozen_ref=frozen_ref
    )

def generator_batteryTemperature(error_rate=0.1, degradation=False, frozen_ref=None):
    if degradation:
        error_rate = min(error_rate * 3, 1.0)

    value = maybe_outlier(
        normal_fn=lambda: round(uniform(20, 35), 4),
        outlier_fn=lambda: round(uniform(35, 45), 4)
    )
    return apply_error(value, error_rate,
        error_weights={'frozen': 0.35, 'drift': 0.30, 'noise': 0.25, 'missing': 0.10},
        frozen_ref=frozen_ref
    )

def generator_powerFactor(error_rate=0.1, degradation=False, frozen_ref=None):
    if degradation:
        error_rate = min(error_rate * 3, 1.0)

    value = maybe_outlier(
        normal_fn=lambda: round(uniform(0.92, 1.0), 4),
        outlier_fn=lambda: round(uniform(0.85, 0.92), 4)
    )
    return apply_error(value, error_rate,
        error_weights={'drift': 0.35, 'bias': 0.30, 'noise': 0.25, 'missing': 0.10},
        frozen_ref=frozen_ref
    )