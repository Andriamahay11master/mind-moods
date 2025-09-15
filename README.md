# 🧠 MindMoods: AI-Powered Text Sentiment Classifier

A lightweight Python AI project that analyzes written text to detect underlying sentiment — **positive, negative, or neutral**.  
This project uses **Natural Language Processing (NLP)** techniques with **TF-IDF vectorization** and a **Logistic Regression model** to classify emotions in real-time user input.

---

## 🚀 Features

- Preprocesses text (tokenization, stopword removal, lowercasing).
- Transforms words into numerical features using **TF-IDF**.
- Classifies sentiment into **Positive / Negative / Neutral**.
- Simple **command-line interface** for user input.
- Ready to extend into a **web app or chatbot**.

---

## 📂 Project Structure

mindmoods-sentiment/
├── data/
├── src/
│ ├── preprocess.py # Text cleaning functions
│ ├── train.py # Model training script
│ ├── predict.py # User input & predictions
├── sentiment_model.pkl # Saved trained model
├── vectorizer.pkl # Saved TF-IDF vectorizer
├── requirements.txt # Project dependencies
├── README.md # Project documentation

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Andriamahay11master/mind-moods.git
   cd mind-moods
   ```
