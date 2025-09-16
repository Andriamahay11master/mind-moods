import tkinter as tk
from tkinter import messagebox
import joblib
from preprocessing import clean_text

# Load model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Function to predict sentiment
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

    # Display sentiment with emoji
    if prediction == "positive":
        result_label.config(text="😊 Positive", fg="green")
    elif prediction == "negative":
        result_label.config(text="😞 Negative", fg="red")
    else:
        result_label.config(text="😐 Neutral", fg="orange")

# Main window
root = tk.Tk()
root.title("MindMoods Sentiment Classifier")
root.geometry("600x300")
root.configure(bg="#f5f5f5")

# Title
title_label = tk.Label(root, text="MindMoods 🧠", font=("Arial", 20, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=10)

# Input Frame
frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(pady=10)

tk.Label(frame, text="Enter your text:", font=("Arial", 12), bg="#f5f5f5").grid(row=0, column=0, padx=5)
entry = tk.Entry(frame, width=50, font=("Arial", 12))
entry.grid(row=0, column=1, padx=5)

# Predict Button
predict_button = tk.Button(root, text="Predict Sentiment 🔍", command=predict_sentiment, font=("Arial", 12, "bold"), bg="#003399", fg="white", relief="solid", bd=1)
predict_button.pack(pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#f5f5f5")
result_label.pack(pady=15)

# Run GUI
root.mainloop()
