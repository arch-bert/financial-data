import sys
from utils import data
from datetime import datetime
from stocks import stock_prices
from crypto import crypto_prices
from currency import forex_rates


############################ RUN WITH TERMINAL ARGUMENTS #################################
#                                             TODO                                       #
#                                                                                        #
##########################################################################################


############################ RUN WITH NO TERMINAL ARGUMENTS ##############################
def main():

    valid = False

    while not valid:

        symbol = input('')


##########################################################################################

def is_valid_symbol(symbol, stocks=True, crypto=False, currency=False):

    try:
        if stocks:
            df = stock_prices.get_time_series(symbol)
        elif crypto:
            df = crypto_prices.get_time_series(symbol)
        elif currency:
            df = forex_rates.get_time_series(symbol)

        return True

    except IndexError:
        print(f"Invalid symbol: '{symbol}'")
        return False


def is_valid_date(date):
    try:
        # Try to parse the date string using format 'YYYY-MM-DD'
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        # If parsing fails, the format is incorrect
        print(f"Invalid date format'{date}'")
        return False


def is_valid_interval(time_step):

    valid_steps = ['1min', '5min', '15min', '30min',
                   '60min', 'daily', 'weekly', 'monthly']

    if time_step in valid_steps or time_step is None:
        return True
    else:
        print(f"Invalid interval: '{time_step}'")
        return False


def is_valid_file_type(file_type):

    if file_type in ['xlsx', 'csv', 'json']:
        return True
    else:
        print(f"Invalid file type: '{file_type}'")
        return False
