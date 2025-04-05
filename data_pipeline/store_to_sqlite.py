import sqlite3
import pandas as pd

def store_to_sqlite():
    df = pd.read_csv("../data/cleaned_mental_health_data.csv")
    conn = sqlite3.connect("../data/mental_health.db")
    df.to_sql("mental_health", conn, if_exists="replace", index=False)
    print("Data stored in SQLite database.")

if __name__ == "__main__":
    store_to_sqlite()
