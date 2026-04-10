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
# ------------------ TRANSFORMATION ------------------
def transform_data(df):
    # Try to find rent column automatically
    rent_col = None
    for col in df.columns:
        if "rent" in col.lower():
            rent_col = col
            break

    if rent_col:
        print("Using rent column:", rent_col)

        df[rent_col] = df[rent_col].astype(str)
        df[rent_col] = df[rent_col].str.replace('[€,]', '', regex=True)

        df[rent_col] = pd.to_numeric(df[rent_col], errors='coerce')
        df = df.dropna(subset=[rent_col])

        df['rent_category'] = df[rent_col].apply(
            lambda x: 'low' if x < 1000 else 'medium' if x < 2000 else 'high'
        )
    else:
        print("No rent column found!")

    return df


# ------------------ DATABASE ------------------
def store_data(df):
    conn = sqlite3.connect("rent_data.db")
    df.to_sql("rent_table", conn, if_exists="append", index=False)
    conn.close()
    print("Data stored in SQLite DB")


# ------------------ PIPELINE ------------------
def run_pipeline():
    csv_url = fetch_dataset()

    if csv_url:
        df = load_data(csv_url)
        df = clean_data(df)
        df = transform_data(df)
        store_data(df)
    else:
        print("No dataset found")


# ------------------ RUN ------------------
if __name__ == "__main__":
    run_pipeline()





