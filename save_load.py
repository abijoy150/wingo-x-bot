# model/save_load.py

from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import os

def load_saved_model(model_path='model/wingo_model.h5'):
    if os.path.exists(model_path):
        return load_model(model_path)
    else:
        print("❌ Model file not found.")
        return None

def load_saved_scaler(scaler_path='model/scaler.npy'):
    if os.path.exists(scaler_path):
        scale = np.load(scaler_path)
        scaler = MinMaxScaler()
        scaler.min_, scaler.scale_ = 0, scale
        return scaler
    else:
        print("❌ Scaler file not found.")
        return None
