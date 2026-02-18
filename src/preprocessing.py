import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def preprocess_data():
    df = pd.read_csv("data/raw/Review_cleaned.csv")
    X = df['review'].values
    y = df['sentiment'].values

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer(max_features=5000)
    X_train_vect = vectorizer.fit_transform(X_train)
    X_test_vect = vectorizer.transform(X_test)

    # Save processed data
    with open("src/preprocessed.pkl", "wb") as f:
        pickle.dump((X_train_vect, X_test_vect, y_train, y_test, vectorizer), f)
    print("Preprocessing completed and saved to preprocessed.pkl")
