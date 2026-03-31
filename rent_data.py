import requests
import pandas as pd

def fetch_dataset():
    url = "https://data.gov.ie/api/3/action/package_search?q=residential%20tenancies"

    response = requests.get(url)
    data = response.json()

    print("Datasets found:", len(data['result']['results']))

    csv_url = None

    for result in data['result']['results']:
        if "tenanc" in result['title'].lower() or "rent" in result['title'].lower():
            for resource in result['resources']:
                if resource['format'].lower() == 'csv':
                    csv_url = resource['url']
                    print("Dataset:", result['title'])
                    print("CSV URL:", csv_url)
                    break
        if csv_url:
            break

    return csv_url


def load_data(csv_url):
    df = pd.read_csv(csv_url)
    print(df.head())
    return df


def save_data(df):
    df.to_csv("rtb_rent_data.csv", index=False)
    print("RTB CSV saved successfully!")


def main():
    csv_url = fetch_dataset()

    if csv_url:
        df = load_data(csv_url)
        save_data(df)
    else:
        print("No CSV dataset found.")


if __name__ == "__main__":
    main()
