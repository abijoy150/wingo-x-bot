# utils/analyzer.py

import pandas as pd
import os
from collections import Counter

def analyze_color_by_hour(file_path='result_log.csv'):
    if not os.path.exists(file_path):
        return {}

    df = pd.read_csv(file_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    analysis = {}

    for hour in range(24):
        colors = df[df['hour'] == hour]['color'].tolist()
        color_count = Counter(colors)
        if color_count:
            dominant_color = color_count.most_common(1)[0][0]
            analysis[hour] = {
                'total': sum(color_count.values()),
                'dominant_color': dominant_color,
                'details': dict(color_count)
            }

    return analysis

def suggest_color_for_current_hour():
    from datetime import datetime
    hour = datetime.now().hour
    analysis = analyze_color_by_hour()
    if hour in analysis:
        return analysis[hour]['dominant_color']
    return "Unknown"
