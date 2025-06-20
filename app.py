from flask import Flask
import threading
import time
from scraper import fetch_latest_result
from model import predict_next_result
from telegram.bot import send_prediction
from scheduler.auto_train import schedule_daily_training

app = Flask(__name__)

def start_prediction_loop():
    last_checked_period = None
    while True:
        try:
            latest_result = fetch_latest_result()
            if not latest_result:
                print("❌ ফলাফল পাওয়া যায়নি, আবার চেষ্টা করছি...")
                time.sleep(5)
                continue

            period = latest_result['period']
            number = latest_result['number']

            if period != last_checked_period:
                prediction = predict_next_result()
                send_prediction(period, prediction)
                last_checked_period = period
                print(f"✅ নতুন ভবিষ্যদ্বাণী পাঠানো হয়েছে: {period}")
            else:
                print("⏳ এখনো নতুন রাউন্ড আসেনি...")

        except Exception as e:
            print(f"❗ Loop error: {str(e)}")

        time.sleep(15)

@app.route('/')
def home():
    return "🚀 Wingo Prediction Bot is Running!"

def run_bot():
    loop_thread = threading.Thread(target=start_prediction_loop)
    loop_thread.start()

if __name__ == '__main__':
    run_bot()
    schedule_daily_training()
    app.run(host='0.0.0.0', port=10000)
