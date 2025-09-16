import tkinter as tk
from tkinter import messagebox
import joblib
from preprocessing import clean_text

# Load model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def predict_sentiment():
    """
    Preprocesses text and predicts sentiment.
    Returns 'positive' or 'negative'.
    """
    text = entry.get()
    if not text.strip():
        messagebox.showwarning("Input Error", "Please enter some text!")
        return
    
    cleaned_text = clean_text(text)
    vectorized_text = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized_text)[0]
    
    result_label.config(text=f"Predicted Sentiment: {prediction.capitalize()}")

# Create GUI window
root = tk.Tk()
root.title("MindMoods Sentiment Classifier")
root.geometry("500x200")

# Input
tk.Label(root, text="Enter your text:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, width=60, font=("Arial", 12))
entry.pack(pady=5)

# Predict Button
predict_button = tk.Button(root, text="Predict Sentiment", command=predict_sentiment, font=("Arial", 12))
predict_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

# Run the GUI
root.mainloop()