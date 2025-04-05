import pandas as pd

def clean_data():
    df = pd.read_csv("../data/raw_mental_health_data.csv")
    df = df[['Indicator', 'Country', 'NumericValue', 'TimeDim']]  # Filter key columns
    df.dropna(inplace=True)
    df.rename(columns={'NumericValue': 'Value', 'TimeDim': 'Year'}, inplace=True)
    df.to_csv("../data/cleaned_mental_health_data.csv", index=False)
    print("Data cleaned and saved.")

if __name__ == "__main__":
    clean_data()
