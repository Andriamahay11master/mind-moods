from flask import Flask, request, jsonify
import joblib
from preprocessing import clean_text

app = Flask(__name__)

# Load model & vectorizer
model = joblib.load("../sentiment_model.pkl")
vectorizer = joblib.load("../vectorizer.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    if not text.strip():
        return jsonify({"error": "Empty input"}), 400

    cleaned = clean_text(text)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]

    return jsonify({"sentiment": prediction})

if __name__ == "__main__":
    app.run(debug=True)
