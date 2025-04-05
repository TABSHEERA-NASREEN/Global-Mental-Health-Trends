import requests
import pandas as pd
import os

def fetch_who_data():
    url = "https://ghoapi.azureedge.net/api/MH_1"
    response = requests.get(url)
    data = response.json()['value']
    df = pd.DataFrame(data)
    df.to_csv("../data/raw_mental_health_data.csv", index=False)
    print("Data fetched and saved.")

if __name__ == "__main__":
    fetch_who_data()
