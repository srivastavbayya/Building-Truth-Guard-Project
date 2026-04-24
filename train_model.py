import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import os

def create_dummy_data():
    data = {
        'text': [
            "Aliens have landed in New York and are giving out free pizza.",
            "The stock market saw a slight increase today following tech earnings.",
            "Drinking bleach cures all known viruses immediately.",
            "Scientists have discovered a new species of frog in the Amazon rainforest.",
            "Eating 50 pounds of chocolate every day leads to immortality.",
            "The local library is hosting a book fair next weekend."
        ],
        'label': [1, 0, 1, 0, 1, 0] # 1 for Fake, 0 for Real
    }
    return pd.DataFrame(data)

def train_and_save_model():
    print("Generating dummy dataset...")
    df = create_dummy_data()

    print("Building the Machine Learning Pipeline...")
    # A simple pipeline with TF-IDF and Logistic Regression
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english')),
        ('clf', LogisticRegression(random_state=42))
    ])

    print("Training the model...")
    pipeline.fit(df['text'], df['label'])

    print("Saving the model to 'truth_guard_model.pkl'...")
    joblib.dump(pipeline, 'truth_guard_model.pkl')
    print("Training complete! You can now run the backend app.")

if __name__ == "__main__":
    train_and_save_model()
