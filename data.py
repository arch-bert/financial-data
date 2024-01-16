import pandas as pd
import requests

API_KEY = 'PNIWMQ39TBLL3JDO'

function = {
    'monthly': ['TIME_SERIES_MONTHLY_ADJUSTED', 'Monthly Adjusted Time Series'],
    'weekly': ['TIME_SERIES_WEEKLY_ADJUSTED', 'Weekly Adjusted Time Series'],
    'daily': ['TIME_SERIES_DAILY_ADJUSTED', 'Time Series (Daily)'],
    '60min': ['TIME_SERIES_INTRADAY', 'Time Series (60min)'],
    '30min': ['TIME_SERIES_INTRADAY', 'Time Series (30min)'],
    '15min': ['TIME_SERIES_INTRADAY', 'Time Series (15min)'],
    '5min': ['TIME_SERIES_INTRADAY', 'Time Series (5min)'],
    '1min': ['TIME_SERIES_INTRADAY', 'Time Series (1min)'],
}

symbol = input('symbol: ')
freq = input('frequency: ')

url = 'https://www.alphavantage.co/query?'
url += f'function={function[freq][0]}'
url += f'&symbol={symbol}'
url += f'&apikey={API_KEY}'

if freq not in ['monthly', 'weekly', 'daily']:
    url += f'&interval={function[freq][1]}'

response = requests.get(url)
data_json = response.json()

if response.status_code == 200:
    json_key = function[freq][1]
    if json_key in data_json:
        df = pd.DataFrame.from_dict(data_json[json_key], orient='index')
        df.index = pd.to_datetime(df.index)
        df.sort_index(inplace=True)
    else:
        print("Time series data not found in the response.")
else:
    print("Failed to fetch data, status code:", response.status_code)

print(df)
