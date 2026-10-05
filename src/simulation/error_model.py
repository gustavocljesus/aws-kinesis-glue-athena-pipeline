from random import random, uniform, gauss, randint
from typing import Callable

OUTLIER_RATE = 0.05
STEP_DRIFT = 0.01    

def apply_error(value: float, error_weights: dict, frozen_ref=None, drift_ref=None):
    error_type = select_error(error_weights)

    if error_type == 'frozen':
        return start_frozen_event(frozen_ref, value)
    elif error_type == 'drift':
        return start_drift_event(drift_ref, value)
    elif error_type == 'bias':
        return bias_error(value)
    elif error_type == 'noise':
        return noise_error(value)
    elif error_type == 'missing':
        return missing_error() 

def select_error(error_weights: dict) -> str:
    chance_error = random()
    cumulative = 0
    etypes = list(error_weights.items())

    for etype, w in etypes[:-1]:
        cumulative += w
        if chance_error <= cumulative:
            return etype
    
    return etypes[-1][0]

def start_frozen_event(frozen_ref: dict, value: float) -> float:
    frozen_ref["is_event"] = True
    frozen_ref["value"] = value
    frozen_ref["episode_duration"] = randint(3, 6) - 1 

    return value

def start_drift_event(drift_ref: dict, value: float) -> float:
    drift_ref["is_event"] = True
    drift_ref["episode_duration"] = randint(6, 10) - 1
    drift_ref["step"] = 0
    drift_ref["accumulation"] = 0
    drift_ref["offset"] = 0.04

    return round(value * (1 + drift_ref["offset"]), 4)

def bias_error(value: float) -> float:
    offset = uniform(-0.03, 0.03) * value  # offset fixo de ±3%
    return round(value + offset, 4)

def noise_error(value: float) -> float:
    return round(gauss(value, value * 0.02), 4)  # ruído gaussiano 2%

def missing_error() -> None:
    return None

def maybe_outlier(normal_fn: Callable[[], float], outlier_fn: Callable[[], float], outlier_rate=OUTLIER_RATE) -> float:
    if random() < outlier_rate:
        return outlier_fn()
    return normal_fn()

def has_active_event(frozen_ref: dict, drift_ref: dict) -> bool:    
    return frozen_ref.get("is_event", False) or drift_ref.get("is_event", False)

def continue_episode(frozen_ref: dict, drift_ref: dict, value: float) -> float:
    if frozen_ref["is_event"]:
        return step_frozen_event(frozen_ref)

    return round(value * (1 + step_drift_event(drift_ref)), 4)

def step_frozen_event(frozen_ref: dict) -> float:
    frozen_ref["episode_duration"] -= 1

    if frozen_ref["episode_duration"] <= 0:
        frozen_ref["is_event"] = False

    return frozen_ref["value"]

def step_drift_event(drift_ref: dict) -> float:
    drift_ref["step"] += 1

    if drift_ref["step"] <= drift_ref["episode_duration"]:
        drift_ref["accumulation"] += 1
        drift_ref["offset"] = round(drift_ref["offset"] + STEP_DRIFT, 4)
    elif drift_ref["accumulation"] > 0:
        drift_ref["accumulation"] -= 1
        drift_ref["offset"] = round(drift_ref["offset"] - STEP_DRIFT, 4)
    else:
        drift_ref["is_event"] = False

    return drift_ref["offset"]