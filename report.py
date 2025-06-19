# utils/report.py

import pandas as pd
import os
from datetime import datetime

def generate_weekly_report(file_path='accuracy_log.csv'):
    if not os.path.exists(file_path):
        return "No accuracy log available."

    df = pd.read_csv(file_path, names=['period', 'predicted', 'actual', 'correct'])
    df['date'] = df['period'].astype(str).str[:8]

    summary = df.groupby('date').agg({
        'correct': ['sum', 'count']
    }).reset_index()

    report = "📅 <b>Weekly Accuracy Report</b>\n\n"
    for index, row in summary.iterrows():
        date = row['date']
        correct = row[('correct', 'sum')]
        total = row[('correct', 'count')]
        accuracy = round((correct / total) * 100, 2) if total else 0
        report += f"🗓️ {date}: {correct}/{total} correct ✅ ({accuracy}%)\n"

    overall_accuracy = round((df['correct'].sum() / len(df)) * 100, 2)
    report += f"\n<b>Overall Accuracy: {overall_accuracy}%</b>\n"
    return report
