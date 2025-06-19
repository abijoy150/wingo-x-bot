# scheduler/retrain.py

import schedule
import time
from model.train_model import train_and_save_model
from telegram.telegram_bot import send_message

def job():
    send_message("🧠 Auto Retrain Started...")
    train_and_save_model()
    send_message("✅ Auto Retrain Complete. New model saved.")

def start_scheduler():
    schedule.every().day.at("06:00").do(job)  # প্রতিদিন সকাল ৬টা
    send_message("📅 Auto Retrain Scheduler Started.")
    while True:
        schedule.run_pending()
        time.sleep(60)
