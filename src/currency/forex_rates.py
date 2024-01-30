from utils.suppress_print import SuppressPrint
from dateutil.parser import ParserError
from openbb_terminal.sdk import openbb
from utils import data


def get_time_series(symbol, start_date=None, end_date=None, interval=None):
    """
    Retrieves time series data for a specified forex pair.

    Parameters:
    - symbol (str): The forex pair symbol, formatted as 'FROM/TO' (e.g., 'USD/EUR').
    - start_date (str, optional): The start date for the time series data. Defaults to None.
    - end_date (str, optional): The end date for the time series data. Defaults to None.
    - interval (str, optional): The interval for the time series data. Can be 'daily', 'monthly', 'weekly', 
      or intra-day intervals like '1min', '5min', etc. Defaults to None (interpreted as 'daily').

    Returns:
    - pandas.DataFrame: A DataFrame containing the requested time series data. Returns None if an error occurs.
    """
    # Split forex pair into two arguments
    from_symbol, to_symbol = symbol.split('/')

    # Load daily time series
    if interval is None or interval == 'daily':
        with SuppressPrint():
            df = openbb.forex.load(from_symbol=from_symbol,
                                   to_symbol=to_symbol,
                                   start_date=start_date,
                                   end_date=end_date)
        data.print_dates_msg(df, start_date, end_date)
    # Load monthly data
    elif interval == 'monthly':
        with SuppressPrint():
            df = openbb.forex.load(from_symbol=from_symbol,
                                   to_symbol=to_symbol,
                                   start_date=start_date,
                                   end_date=end_date,
                                   interval='1month')
        data.print_dates_msg(df, start_date, end_date)
    # Load weekly data
    elif interval == 'weekly':
        with SuppressPrint():
            df = openbb.forex.load(from_symbol=from_symbol,
                                   to_symbol=to_symbol,
                                   start_date=start_date,
                                   end_date=end_date,
                                   interval='1week')
        data.print_dates_msg(df, start_date, end_date)
    # Load intra-day data
    elif interval in ['1min', '5min', '15min', '30min', '60min']:
        with SuppressPrint():
            int(interval.replace('min', ''))
            df = openbb.forex.load(from_symbol=from_symbol,
                                   to_symbol=to_symbol,
                                   start_date=start_date,
                                   end_date=end_date,
                                   interval=interval)
            data.print_dates_msg(df, start_date, end_date)
    # Handle invalid time-step ()
    else:
        print(f"Invalid time-step: '{interval}'")
        return None

    return df
