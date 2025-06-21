from model.predictor import predict_next_result  # 🔁 এটিই সঠিক

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    prediction = predict_next_result()
    return f"""
    <h2>🎯 Wingo Prediction</h2>
    <p>Period: {prediction['period']}</p>
    <p>Result: {prediction['number']} ({prediction['size']})</p>
    <p>Color: {prediction['color']}</p>
    <p>Confidence: {prediction['confidence']}%</p>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
