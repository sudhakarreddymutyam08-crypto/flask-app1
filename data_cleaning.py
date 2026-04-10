import requests
import pandas as pd
import sqlite3

# ------------------ DATA ACQUISITION ------------------
def fetch_dataset():
    url = "https://data.gov.ie/api/3/action/package_search?q=residential%20tenancies"
    response = requests.get(url)
    data = response.json()

    csv_url = None

    for result in data['result']['results']:
        if "tenanc" in result['title'].lower() or "rent" in result['title'].lower():
            for resource in result['resources']:
                if resource['format'].lower() == 'csv':
                    csv_url = resource['url']
                    break
        if csv_url:
            break

    return csv_url
def load_data(csv_url):
    df = pd.read_csv(csv_url)
    print("Loaded shape:", df.shape)
    print("Columns:", df.columns)   # IMPORTANT (to debug column names)
    return df


# ------------------ CLEANING ------------------
def clean_data(df):
    print("Before cleaning:", df.shape)
    df = df.dropna()
    df = df.drop_duplicates()
    print("After cleaning:", df.shape)
    return df

