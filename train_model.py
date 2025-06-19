# model/train_model.py

import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import os

def load_data(file_path='result_log.csv'):
    if not os.path.exists(file_path):
        print("No data file found for training.")
        return None, None
    df = pd.read_csv(file_path)
    if 'number' not in df.columns:
        print("CSV does not contain 'number' column.")
        return None, None
    return df[['number']], df['number']

def prepare_sequences(data, sequence_length=10):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)

    X, y = [], []
    for i in range(sequence_length, len(scaled_data)):
        X.append(scaled_data[i-sequence_length:i])
        y.append(scaled_data[i])
    return np.array(X), np.array(y), scaler

def train_and_save_model():
    df, _ = load_data()
    if df is None:
        return

    X, y, scaler = prepare_sequences(df)

    model = Sequential()
    model.add(LSTM(64, activation='relu', input_shape=(X.shape[1], X.shape[2])))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')

    model.fit(X, y, epochs=10, verbose=1)

    model.save('model/wingo_model.h5')
    np.save('model/scaler.npy', scaler.scale_)
    print("✅ Model training complete and saved.")
