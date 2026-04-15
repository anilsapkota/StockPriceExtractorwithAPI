import requests
import openai
import os
import time

from dotenv import load_dotenv
load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
print("API Key:", POLYGON_API_KEY)

limit = 4
tickers = []
url = f'https://api.massive.com/v3/reference/tickers?market=stocks&active=true&order=asc&limit={limit}&sort=ticker&apiKey={POLYGON_API_KEY}'



response = requests.get(url)
data = response.json()
print(data.keys())
print(data['next_url'])

for ticker in data['results']:
    tickers.append(ticker)


while 'next_url' in data:
    time.sleep(12)  # free tier allows ~5 requests/min
    print("Fetching more results...")
    response = requests.get(data['next_url'] + f'&apiKey={POLYGON_API_KEY}')
    data = response.json()

    if 'results' not in data:
        print("Unexpected response:", data)
        break

    for ticker in data['results']:
        tickers.append(ticker)

print(len(tickers))