import pandas as pd
import requests

API_KEY = 'PNIWMQ39TBLL3JDO'

function = {'monthly': ['TIME_SERIES_MONTHLY_ADJUSTED', ''],
            'weekly': ['TIME_SERIES_WEEKLY_ADJUSTED', ''],
            'daily': ['TIME_SERIES_DAILY_ADJUSTED', ''],
            '60min': ['TIME_SERIES_INTRADAY', '60min'],
            '30min': ['TIME_SERIES_INTRADAY', '30min'],
            '15min': ['TIME_SERIES_INTRADAY', '15min'],
            '5min': ['TIME_SERIES_INTRADAY', '5min'],
            '1min': ['TIME_SERIES_INTRADAY', '1min'],
            }

interval = {1: '1min', 5: '5min', 15: '15min', 30: '30min', 60: '60min'}

symbol = input('symbol: ')
freq = input('frequency: ')
start_date = input('start_date: ')
end_date = input('end_date: ')

url = 'https://www.alphavantage.co/query?'
url += f'function={function[freq][0]}'
url += f'&symbol={symbol}'
url += f'&apikey={API_KEY}'

if not (freq == 'monthly' or freq == 'weekly' or freq == 'daily'):
    url += f'&interval={function[freq][1]}'
