# src/preprocessing.py
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK data (only needed once)
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Initialize stopwords and lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text, lemmatize=True):
    """
    Cleans the input text:
    - Converts to lowercase
    - Removes punctuation and numbers
    - Removes stopwords
    - Optionally lemmatizes words
    """
    # Lowercase
    text = text.lower()
    
    # Remove punctuation and numbers
    text = re.sub(r'[^a-z\s]', '', text)
    
    # Tokenize
    words = text.split()
    
    # Remove stopwords
    words = [word for word in words if word not in stop_words]
    
    # Lemmatize (optional)
    if lemmatize:
        words = [lemmatizer.lemmatize(word) for word in words]
    
    return ' '.join(words)

# Example usage
if __name__ == "__main__":
    sample_text = "I loved the movie! It was amazing and fun."
    print("Original:", sample_text)
    print("Cleaned:", clean_text(sample_text))
    print("Cleaned (lemmatized):", clean_text(sample_text, lemmatize=True))