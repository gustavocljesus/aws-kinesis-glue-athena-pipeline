import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="AWS Pipeline FarmWind")
    parser.add_argument("-r", "--ramp-duration", type=positive_int, default=300,
                        help="Duration of the degradation ramp period in seconds (default: 300 = 5min)")
    parser.add_argument("-s", "--sleep", type=non_negative_float, default=2, help="Interval between sending batches in seconds (default: 2)")
    
    return parser.parse_args()

def positive_int(value):
    n = int(value)

    if n <= 0:
        raise argparse.ArgumentTypeError(f"{value} must be greater than 0.")
    return n

def non_negative_float(value):
    n = float(value)

    if n < 0:
        raise argparse.ArgumentTypeError(f"{value} must be greater than or equal to 0.")
    return n

