# utils/dashboard.py

from flask import Flask, render_template_string
import pandas as pd
import os
from utils.report import generate_weekly_report
from utils.accuracy import get_accuracy

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Wingo Predictor Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f8f8f8; padding: 30px; }
        h1 { color: #333; }
        .card { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 20px; }
        .report { white-space: pre-line; font-family: monospace; }
    </style>
</head>
<body>
    <h1>📊 Wingo Prediction Dashboard</h1>
    
    <div class="card">
        <h2>✅ Accuracy Overview</h2>
        <p>Total Predictions: <b>{{ total }}</b><br>
           Correct Predictions: <b>{{ correct }}</b><br>
           Accuracy: <b>{{ accuracy }}%</b></p>
    </div>

    <div class="card">
        <h2>📅 Weekly Summary</h2>
        <div class="report">{{ report }}</div>
    </div>
</body>
</html>
"""

@app.route('/')
def dashboard():
    total, correct = get_accuracy()
    accuracy = round((correct / total) * 100, 2) if total > 0 else 0
    report = generate_weekly_report()
    return render_template_string(TEMPLATE, total=total, correct=correct, accuracy=accuracy, report=report)

def run_dashboard():
    app.run(host="0.0.0.0", port=10000)
