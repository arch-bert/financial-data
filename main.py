import sys
from utils import data
from datetime import datetime
from stocks import stock_prices
from crypto import crypto_prices
from currency import forex_rates
from utils.suppress_print import SuppressPrint


###################### MAIN LOOP ######################
def main():
    # Initialize variables
    data_type = None
    symbol = None
    start_date = None
    end_date = None
    interval = None
    format = None

    # Data type input loop
    valid = False
    while not valid:
        data_type = input('Financial data type {stocks, crypto, forex}:   ')
        valid = is_valid_data_type(data_type)

    # Symbol input loop
    valid = False
    while not valid:

        symbol = input('Symbol {<TICKER>}:   ')
        if data_type == 'stocks':
            valid = is_valid_symbol(symbol, stocks=True)
        elif data_type == 'crypto':
            valid = is_valid_symbol(symbol, crypto=True)
        else:
            valid = is_valid_symbol(symbol, currency=True)

    # Start date input loop
    valid = False
    while not valid:
        start_date = input('Start date {YYYY-MM-DD}:   ')
        valid = is_valid_date(start_date)

    # End date input loop
    valid = False
    while not valid:
        end_date = input('End date {YYYY-MM-DD}:   ')
        valid = is_valid_date(end_date)

    # Interval input loop
    valid = False
    while not valid:
        valid_intervals = "'1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly'"
        interval = input(f"Interval {valid_intervals}:   ")
        valid = is_valid_interval(interval)

    # Format input loop
    valid = False
    while not valid:
        format = input("Format {xlsx, csv, json}:   ")
        valid = is_valid_format(format)

    # Pull data using valid input
    if data_type == 'stocks':
        df = stock_prices.get_time_series(symbol, start_date,
                                          end_date, interval)
    elif data_type == 'crypto':
        df = crypto_prices.get_time_series(symbol, start_date,
                                           end_date, interval)
    else:
        df = forex_rates.get_time_series(symbol, start_date,
                                         end_date, interval)

    # Clean currency symbol for filename
    symbol = symbol.replace('/', '_')

    # Get actual time-series dates
    actual_start_date = df.index[0]
    actual_end_date = df.index[-1]
    # Remove time from the DateTime object
    actual_start_date = actual_start_date.strftime('%Y-%m-%d', )
    actual_end_date = actual_end_date.strftime('%Y-%m-%d')

    # Create filename string
    file_name = f'{symbol}_{actual_start_date}_{actual_end_date}_{interval}'

    # Clean DataFrame and write to file
    data.clean_data_frame(df)
    data.write_to_file(df, file_name, format)

###################### FUNCTIONS ######################


def is_valid_data_type(data_type):

    if data_type in ['stocks', 'crypto', 'forex']:
        return True
    else:
        print(f"Invalid financial data type: '{data_type}'")
        return False


def is_valid_symbol(symbol, stocks=True, crypto=False, currency=False):

    try:
        if stocks:
            with SuppressPrint():
                df = stock_prices.get_time_series(symbol)
        elif crypto:
            with SuppressPrint():
                df = crypto_prices.get_time_series(symbol)
        elif currency:
            with SuppressPrint():
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

    valid_intervals = ['1min', '5min', '15min', '30min',
                       '60min', 'daily', 'weekly', 'monthly']

    if time_step in valid_intervals or time_step is None:
        return True
    else:
        print(f"Invalid interval: '{time_step}'")
        return False


def is_valid_format(format):

    if format in ['xlsx', 'csv', 'json']:
        return True
    else:
        print(f"Invalid file type: '{format}'")
        return False


if __name__ == '__main__':
    main()
