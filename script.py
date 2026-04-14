import requests
import openai
import os 

from dotenv import load_dotenv
load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
print("API Key:", POLYGON_API_KEY)


tickers = []
url = f'https://api.massive.com/v3/reference/tickers?market=stocks&active=true&order=asc&limit=100&sort=ticker&apiKey={POLYGON_API_KEY}'



response = requests.get(url)
data = response.json()
print(data.keys())

for ticker in data['results']:
    tickers.append(ticker)

print((tickers))