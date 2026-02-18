import pandas as pd

def clean_data():
    df = pd.read_csv("data/raw/Review.csv")
    # Example cleaning: drop duplicates, remove empty rows
    df = df.drop_duplicates()
    df = df.dropna()
    df.to_csv("data/raw/Review_cleaned.csv", index=False)
    print("Data cleaned and saved as Review_cleaned.csv")
