# src/predict.py

import joblib
from preprocessing import clean_text

# Load the saved model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def predict_sentiment(text):
    """
    Preprocesses text and predicts sentiment.
    Returns 'positive' or 'negative'.
    """
    cleaned_text = clean_text(text)
    vectorized_text = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized_text)
    return prediction[0]

if __name__ == "__main__":
    print("Welcome to MindMoods Sentiment Predictor!")
    print("Type 'quit' to exit.\n")
    
    while True:
        user_input = input("Enter a sentence: ")
        if user_input.lower() == 'quit':
            print("Exiting...")
            break
        sentiment = predict_sentiment(user_input)
        print(f"Predicted Sentiment: {sentiment}\n")
