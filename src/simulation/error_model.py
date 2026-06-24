from random import random, uniform, gauss

OUTLIER_RATE = 0.05  

def apply_error(value, error_rate, error_weights=None, frozen_ref=None):
    """
    error_weights: dict com pesos por tipo. Ex: {'frozen': 0.5, 'drift': 0.3, 'missing': 0.2}
    frozen_ref: valor de referência para simular sensor travado
    """
    if random() >= error_rate:
        if frozen_ref is not None:
            frozen_ref["value"] = value 
        return value

    default_weights = {
        'frozen':  0.30,
        'drift':   0.25,
        'bias':    0.20,
        'noise':   0.15,
        'missing': 0.10,
    }
    weights = {**default_weights, **(error_weights or {})}

    # escolha ponderada manual
    r = random()
    cumulative = 0
    for etype, w in weights.items():
        cumulative += w
        if r <= cumulative:
            error_type = etype
            break

    if error_type == 'frozen':
        if frozen_ref is not None and frozen_ref.get("value") is not None:
            return frozen_ref["value"]
        else:
            return value

    elif error_type == 'drift':
        drift = uniform(0.01, 0.05) * value  # deriva de 1% a 5%
        return round(value + drift, 4)

    elif error_type == 'bias':
        offset = uniform(-0.03, 0.03) * value  # offset fixo de ±3%
        return round(value + offset, 4)

    elif error_type == 'noise':
        return round(gauss(value, value * 0.02), 4)  # ruído gaussiano 2%

    elif error_type == 'missing':
        return None

    return value

def maybe_outlier(normal_fn, outlier_fn, outlier_rate=OUTLIER_RATE):
    if random() < outlier_rate:
        return outlier_fn()
    return normal_fn()