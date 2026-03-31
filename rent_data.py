import requests

url = "https://data.gov.ie/api/3/action/package_search?q=rent"

response = requests.get(url)
data = response.json()

for result in data['result']['results'][:3]:
    print("Title:", result['title'])
    print("Organization:", result['organization']['title'])
    print("-"*40)
