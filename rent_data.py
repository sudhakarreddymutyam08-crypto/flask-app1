import requests
import pandas as pd

# API call
url = "https://data.gov.ie/api/3/action/package_search?q=rent"

response = requests.get(url)
data = response.json()

# Print datasets
for result in data['result']['results'][:5]:
    print("Title:", result['title'])
    print("Organization:", result['organization']['title'])
    print("-"*40)

# Extract CSV
csv_url = None

for result in data['result']['results']:
    for resource in result['resources']:
        if resource['format'].lower() == 'csv':
            csv_url = resource['url']
            break
    if csv_url:
        break

print("Using CSV:", csv_url)

# Load data
df = pd.read_csv(csv_url)

print(df.head())

# Save CSV
df.to_csv("rent_data.csv", index=False)

print("CSV saved successfully!")
