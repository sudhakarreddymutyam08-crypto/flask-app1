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


