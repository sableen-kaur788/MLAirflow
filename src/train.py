import pickle
from sklearn.linear_model import LogisticRegression

def train_model():
    with open("mlpipeline/src/preprocessed.pkl", "rb") as f:
        X_train, X_test, y_train, y_test, vectorizer = pickle.load(f)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Save trained model
    with open("mlpipeline/models/model.pkl", "wb") as f:
        pickle.dump(model, f)

    # Optional: evaluate
    acc = model.score(X_test, y_test)
    print(f"Model trained. Accuracy on test set: {acc:.4f}")
