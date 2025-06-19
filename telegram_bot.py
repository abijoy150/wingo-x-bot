# telegram/telegram_bot.py

import requests
from config import BOT_TOKEN, CHAT_ID

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print("❌ Telegram Error:", response.text)
    except Exception as e:
        print("❌ Telegram Exception:", e)

def format_prediction(predicted_number):
    color = get_color(predicted_number)
    size = "Big" if predicted_number >= 5 else "Small"
    return f"<b>🔮 Predicted Result</b>\nNumber: <b>{predicted_number}</b>\nColor: <b>{color}</b>\nSize: <b>{size}</b>"

def format_result(result):
    return f"📢 <b>Official Result</b>\nPeriod: <code>{result['period']}</code>\nNumber: <b>{result['number']}</b>\nColor: <b>{result['color']}</b>\nSize: <b>{result['size']}</b>\n🕒 {result['timestamp']}"

def format_accuracy(total, correct):
    percent = round((correct / total) * 100, 2) if total > 0 else 0
    return f"✅ Accuracy Update:\nTotal: {total}\nCorrect: {correct}\nAccuracy: <b>{percent}%</b>"

def get_color(number):
    if number in [1, 3, 7, 9]:
        return "Green"
    elif number in [2, 4, 6, 8]:
        return "Red"
    elif number in [0, 5]:
        return "Violet"
    return "Unknown"
