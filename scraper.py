# scraper/scraper.py

import requests
from datetime import datetime

from config import WINGO_URL

def fetch_latest_result():
    try:
        response = requests.get(WINGO_URL, timeout=5)
        data = response.json()

        if 'result' in data and data['result']:
            latest = data['result'][0]
            period = latest['period']
            number = int(latest['number'])
            color = get_color(number)
            size = "Big" if number >= 5 else "Small"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            return {
                "period": period,
                "number": number,
                "color": color,
                "size": size,
                "timestamp": timestamp
            }
        return None
    except Exception as e:
        print("Error fetching result:", e)
        return None

def get_color(number):
    if number in [1, 3, 7, 9]:
        return "Green"
    elif number in [2, 4, 6, 8]:
        return "Red"
    elif number in [0, 5]:
        return "Violet"
    return "Unknown"
