from flask import Flask
from model.predictor import predict_next_result

app = Flask(__name__)

@app.route('/')
def home():
    prediction = predict_next_result()

    # Default values if keys are missing
    period = prediction.get('period', '❓ Not Available')
    result = prediction.get('result', '❓ Not Available')
    color = prediction.get('color', '❓ Not Available')

    return f"""
        <h1>🔮 Wingo 1-Minute Prediction</h1>
        <p><strong>Period:</strong> {period}</p>
        <p><strong>Result:</strong> {result}</p>
        <p><strong>Color:</strong> {color}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
