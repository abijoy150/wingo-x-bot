# app.py

import time
import threading
from scraper.scraper import fetch_latest_result
from model.predict_model import predict_next
from utils.accuracy import log_prediction, get_accuracy
from telegram.telegram_bot import send_message, format_result, format_prediction, format_accuracy
from utils.dashboard import run_dashboard
from scheduler.retrain import start_scheduler
import pandas as pd
import os

RESULT_LOG = "result_log.csv"

def save_result(result):
    # CSV তে রেজাল্ট লগ করা
    if not os.path.exists(RESULT_LOG):
        df = pd.DataFrame(columns=["period", "number", "color", "size", "timestamp"])
        df.to_csv(RESULT_LOG, index=False)
    df = pd.read_csv(RESULT_LOG)
    if result['period'] not in df['period'].values:
        df = df.append(result, ignore_index=True)
        df.to_csv(RESULT_LOG, index=False)

def main_loop():
    last_period = None
    while True:
        result = fetch_latest_result()
        if result and result['period'] != last_period:
            last_period = result['period']
            save_result(result)

            predicted_number = predict_next()
            if predicted_number is None:
                send_message("❌ Prediction model not ready.")
                time.sleep(30)
                continue

            # Accuracy log update
            log_prediction(result['period'], predicted_number, result['number'])

            # Send Telegram messages
            send_message(format_result(result))
            send_message(format_prediction(predicted_number))

            total, correct = get_accuracy()
            send_message(format_accuracy(total, correct))

        time.sleep(30)  # ৩০ সেকেন্ড পর পর চেক করবে

def start_bot():
    bot_thread = threading.Thread(target=main_loop)
    bot_thread.daemon = True
    bot_thread.start()

def start_dashboard_server():
    dash_thread = threading.Thread(target=run_dashboard)
    dash_thread.daemon = True
    dash_thread.start()

def start_retrain_scheduler():
    scheduler_thread = threading.Thread(target=start_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()

if __name__ == "__main__":
    send_message("🤖 Wingo Prediction Bot Started.")
    start_bot()
    start_dashboard_server()
    start_retrain_scheduler()
    while True:
        time.sleep(1)
