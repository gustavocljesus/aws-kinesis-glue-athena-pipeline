from random import random, choice

OUTLIER_RATE = 0.05

def apply_error(value, error_rate):
    if random() < error_rate:
        error_type = choice(['type_error', 'missing', 'invalid_value'])
        
        if error_type == 'type_error':
            return str(value)
        elif error_type == 'missing':
            return None
        elif error_type == 'invalid_value':
            return -999
    
    return value

def maybe_outlier(normal_fn, outlier_fn, outlier_rate=OUTLIER_RATE):
    if random() < outlier_rate:
        return outlier_fn()
    return normal_fn()