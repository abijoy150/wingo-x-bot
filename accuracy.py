# utils/accuracy.py

import csv
import os

ACCURACY_FILE = "accuracy_log.csv"

def log_prediction(period, predicted, actual):
    is_correct = int(predicted == actual)
    with open(ACCURACY_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([period, predicted, actual, is_correct])

def get_accuracy():
    if not os.path.exists(ACCURACY_FILE):
        return 0, 0
    total, correct = 0, 0
    with open(ACCURACY_FILE, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 4:
                total += 1
                correct += int(row[3])
    return total, correct

def reset_accuracy_log():
    if os.path.exists(ACCURACY_FILE):
        os.remove(ACCURACY_FILE)
