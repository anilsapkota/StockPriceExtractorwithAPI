import requests
import openai
import os
import time
import csv

from dotenv import load_dotenv
load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

limit = 1000


def run_stock_job():
    tickers = []
    url = f'https://api.massive.com/v3/reference/tickers?market=stocks&active=true&order=asc&limit={limit}&sort=ticker&apiKey={POLYGON_API_KEY}'

    response = requests.get(url)
    data = response.json()
    print(data.keys())
    print(data['next_url'])

    for ticker in data['results']:
        tickers.append(ticker)

    while 'next_url' in data:
        time.sleep(15)  # free tier allows ~5 requests/min
        print("Fetching more results...")
        response = requests.get(data['next_url'] + f'&apiKey={POLYGON_API_KEY}')
        data = response.json()

        if 'results' not in data:
            print("Unexpected response:", data)
            break

        for ticker in data['results']:
            tickers.append(ticker)

    example_ticker = tickers[0]
    print("Example Ticker:", example_ticker)

    fieldnames = list(example_ticker.keys())
    print(fieldnames)

    output_csv = 'tickers.csv'
    with open(output_csv, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for t in tickers:
            row = {key: t.get(key, '') for key in fieldnames}
            writer.writerow(row)

    print(f'Wrote {len(tickers)} rows to {output_csv}')


if __name__ == '__main__':
    run_stock_job
