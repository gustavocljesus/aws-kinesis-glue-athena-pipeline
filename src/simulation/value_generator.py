from random import uniform, random
from .error_model import apply_error, maybe_outlier, has_active_event, continue_episode

def generator_hydraulicPressure(tax, seconds_elapsed, frozen_ref=None, drift_ref=None):
    ERROR_WEIGHTS = {'missing': 0.40, 'frozen': 0.30, 'bias': 0.20, 'drift': 0.10}

    return simulate_reading(
        normal_range=(150, 180),
        outlier_range=(180, 200),
        error_weights=ERROR_WEIGHTS,
        tax=tax,
        seconds_elapsed=seconds_elapsed,
        frozen_ref=frozen_ref,
        drift_ref=drift_ref
    )

def generator_batteryTemperature(tax, seconds_elapsed, frozen_ref=None, drift_ref=None):
    ERROR_WEIGHTS = {'frozen': 0.35, 'drift': 0.30, 'noise': 0.25, 'missing': 0.10}

    return simulate_reading(
        normal_range=(20, 35),
        outlier_range=(35, 45),
        error_weights=ERROR_WEIGHTS,
        tax=tax,
        seconds_elapsed=seconds_elapsed,
        frozen_ref=frozen_ref,
        drift_ref=drift_ref
    )

def generator_powerFactor(tax, seconds_elapsed, frozen_ref=None, drift_ref=None):
    ERROR_WEIGHTS = {'drift': 0.35, 'bias': 0.30, 'noise': 0.25, 'missing': 0.10}

    return simulate_reading(
        normal_range=(0.92, 1.0),
        outlier_range=(0.85, 0.92),
        error_weights=ERROR_WEIGHTS,
        tax=tax,
        seconds_elapsed=seconds_elapsed,
        frozen_ref=frozen_ref,
        drift_ref=drift_ref
    )

def simulate_reading(normal_range, outlier_range, *, error_weights, tax, seconds_elapsed, frozen_ref, drift_ref):
    ERROR_RATE = min(0.1 + tax * seconds_elapsed, 0.3)

    value = maybe_outlier(
        normal_fn=lambda: round(uniform(*normal_range), 4),
        outlier_fn=lambda: round(uniform(*outlier_range), 4)
    )

    if frozen_ref is not None and drift_ref is not None and has_active_event(frozen_ref, drift_ref):
        return continue_episode(frozen_ref, drift_ref, value)

    if random() <= ERROR_RATE:
        return apply_error(
            value,
            error_weights=error_weights,
            frozen_ref=frozen_ref,
            drift_ref=drift_ref
        )
    return value