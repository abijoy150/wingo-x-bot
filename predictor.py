import random

def predict_next_result():
    prediction = {
        "period": "202506211200",
        "number": random.randint(0, 9),
        "size": random.choice(["Big", "Small"]),
        "color": random.choice(["Red", "Green", "Violet"]),
        "confidence": random.randint(80, 99)
    }
    return prediction
