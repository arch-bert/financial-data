from utils import data
from datetime import datetime
from stocks import stock_prices
from crypto import crypto_prices
from currency import forex_rates
from utils.suppress_print import SuppressPrint


###################### MAIN LOOP ######################
def main():
    """
    The main loop for the financial data extraction script. This function prompts the user for input
    on the type of financial data needed (stocks, crypto, forex), the symbol for the data,
    the start and end dates for the data range, the interval of the data, and the desired output format.
    It then fetches the data and saves it to a file.
    """

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
    """
    Validates the financial data type input by the user.

    Parameters:
    - data_type (str): The type of financial data the user wants to fetch (stocks, crypto, forex).

    Returns:
    - bool: True if the data_type is valid, False otherwise.
    """

    if data_type in ['stocks', 'crypto', 'forex']:
        return True
    else:
        print(f"Invalid financial data type: '{data_type}'")
        return False


def is_valid_symbol(symbol, stocks=False, crypto=False, currency=False):
    """
    Validates the symbol input by the user based on the type of financial data.

    Parameters:
    - symbol (str): The symbol for the financial data (like a stock ticker).
    - stocks (bool): Flag to indicate stock symbol validation. Default is True.
    - crypto (bool): Flag to indicate cryptocurrency symbol validation. Default is False.
    - currency (bool): Flag to indicate forex symbol validation. Default is False.

    Returns:
    - bool: True if the symbol is valid, False otherwise.
    """

    try:
        if stocks:
            print(symbol)
            with SuppressPrint():
                df = stock_prices.get_time_series(symbol)
        elif crypto:
            with SuppressPrint():
                df = crypto_prices.get_time_series(symbol)
        elif currency:
            print(symbol)
            with SuppressPrint():
                df = forex_rates.get_time_series(symbol)

        return True

    except IndexError:
        print(f"Invalid symbol: '{symbol}'")
        return False


def is_valid_date(date):
    """
    Validates the date input by the user.

    Parameters:
    - date (str): The date string to validate, expected in 'YYYY-MM-DD' format.

    Returns:
    - bool: True if the date format is valid, False otherwise.
    """

    try:
        # Try to parse the date string using format 'YYYY-MM-DD'
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        # If parsing fails, the format is incorrect
        print(f"Invalid date format'{date}'")
        return False


def is_valid_interval(time_step):
    """
    Validates the interval input by the user.

    Parameters:
    - time_step (str): The interval for the financial data (e.g., '1min', '5min', etc.).

    Returns:
    - bool: True if the interval is valid, False otherwise.
    """

    valid_intervals = ['1min', '5min', '15min', '30min',
                       '60min', 'daily', 'weekly', 'monthly']

    if time_step in valid_intervals or time_step is None:
        return True
    else:
        print(f"Invalid interval: '{time_step}'")
        return False


def is_valid_format(format):
    """
    Validates the file format input by the user.

    Parameters:
    - format (str): The format for output file (e.g., 'xlsx', 'csv', 'json').

    Returns:
    - bool: True if the file format is valid, False otherwise.
    """

    if format in ['xlsx', 'csv', 'json']:
        return True
    else:
        print(f"Invalid file type: '{format}'")
        return False


if __name__ == '__main__':
    main()
