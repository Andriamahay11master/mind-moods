# MindMoods: AI-Powered Text Sentiment Classifier

A lightweight Python AI project that analyzes written text to detect underlying sentiment — positive, negative, or neutral. It uses natural language preprocessing with TF-IDF and a machine learning model (Logistic Regression) to classify emotions in real-time user input.

---

## 🚀 Features

- Cleaned and preprocessed text data using NLP techniques.
- TF-IDF vectorization to represent text numerically.
- Trained a Logistic Regression model for sentiment classification.
- Interactive console-based predictions from user input.
- Easy-to-understand project for AI beginners.

---

## 📂 Project Structure

MindMoods/
│
├── data/ # Dataset folder (CSV or text files)  
├── notebooks/ # Jupyter notebooks for experiments  
├── src/ # Python source code  
│ ├── preprocessing.py # Text cleaning and preprocessing functions  
│ ├── train.py # Model training script  
│ ├── predict.py # Prediction script for user input  
│
├── requirements.txt # List of dependencies  
├── README.md # Project documentation

---

## ⚙️ Installation

# Clone the repository

git clone https://github.com/Andriamahay11master/mind-moods.git

# Navigate into the folder

cd mind-moods

# Create a virtual environment (optional but recommended)

python -m venv venv  
source venv/bin/activate # On Mac/Linux  
venv\Scripts\activate # On Windows

# Install dependencies

pip install -r requirements.txt

---

## 🛠️ Technologies Used

- **Python 3.9+**
- **scikit-learn** (for model building)
- **pandas & numpy** (for data handling)
- **NLTK** (for text preprocessing)
- **Jupyter Notebook** (for experimentation)

---

## ▶️ Usage

# Train the model

python src/train.py

# Make a prediction

python src/predict.py

Example interaction:  
Enter a sentence: "I love learning AI!"  
Predicted Sentiment: Positive

---

## 👨‍💻 Author

**Andriamahay Henikaja IRIMANANA**

- Portfolio: [https://andriamahay-irimanana.vercel.app/]
- LinkedIn: [https://www.linkedin.com/in/andriamahay-henikaja-irimanana/]
- GitHub: [https://github.com/Andriamahay11master]
