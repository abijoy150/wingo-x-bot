# model/predict_model.py

import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import os

def load_recent_data(file_path='result_log.csv', sequence_length=10):
    if not os.path.exists(file_path):
        return None
    df = pd.read_csv(file_path)
    if len(df) < sequence_length:
        return None
    return df['number'].values[-sequence_length:]

def load_scaler():
    scale = np.load('model/scaler.npy')
    scaler = MinMaxScaler()
    scaler.min_, scaler.scale_ = 0, scale
    return scaler

def predict_next():
    recent = load_recent_data()
    if recent is None:
        return None

    model = load_model('model/wingo_model.h5')
    scaler = load_scaler()

    input_seq = scaler.transform(np.array(recent).reshape(-1, 1))
    input_seq = np.expand_dims(input_seq, axis=0)

    prediction = model.predict(input_seq)
    predicted_number = scaler.inverse_transform(prediction)[0][0]
    return round(predicted_number)
