import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib
from preprocessing import clean_text

# 1. Load dataset
data = pd.read_csv('data/IMDB Dataset.csv') 
# Make sure the dataset has 'review' and 'sentiment' columns
# sentiment: e.g., 'positive'/'negative'

# 2. Clean text
data['cleaned_review'] = data['review'].apply(lambda x: clean_text(str(x)))

# 3. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    data['cleaned_review'],
    data['sentiment'],
    test_size=0.2,
    random_state=42
)

# 4. TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# 5. Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

# 6. Evaluate
y_pred = model.predict(X_test_tfidf)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 7. Save model and vectorizer
joblib.dump(model, 'sentiment_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Model and vectorizer saved successfully!")
