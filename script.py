import requests
import openai
import os 

from dotenv import load_dotenv
load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
print("API Key:", POLYGON_API_KEY)

limit = 100
tickers = []
url = f'https://api.massive.com/v3/reference/tickers?market=stocks&active=true&order=asc&limit={limit}&sort=ticker&apiKey={POLYGON_API_KEY}'



response = requests.get(url)
data = response.json()
print(data.keys())
print(data['next_url'])

for ticker in data['results']:
    tickers.append(ticker)

print(len(tickers))