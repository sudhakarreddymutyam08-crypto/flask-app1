import requests

url = "https://data.gov.ie/api/3/action/package_search?q=rent"

response = requests.get(url)
data = response.json()

for result in data['result']['results'][:3]:
    print("Title:", result['title'])
    print("Organization:", result['organization']['title'])
    print("-"*40)
    
import pandas as pd

url = "https://docs.google.com/spreadsheets/d/1IUVKA-a4fblWawCmlhJyTrQZ3e1R1Nvm3D9bXksk0GM/gviz/tq?tqx=out:csv&gid=0"

df = pd.read_csv(url)

print(df.head())
