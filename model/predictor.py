# model/predictor.py

import random

def predict_next_result(previous_results=[]):
    # Dummy prediction logic for now
    result_number = random.randint(0, 9)
    color = "Green" if result_number in [1, 3, 7, 9] else "Red" if result_number in [2, 4, 6, 8] else "Violet"
    size = "Big" if result_number >= 5 else "Small"
    return {
        "number": result_number,
        "color": color,
        "size": size
    }
