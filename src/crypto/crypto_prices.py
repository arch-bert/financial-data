from utils.suppress_print import SuppressPrint
from dateutil.parser import ParserError
from openbb_terminal.sdk import openbb
from utils import data


def get_time_series(symbol, start_date=None, end_date=None, interval=None):
    """
    Retrieves time series data for a given cryptocurrency symbol.

    Parameters:
    - symbol (str): The symbol of the cryptocurrency to retrieve data for.
    - start_date (str, optional): The start date for the time series data. Defaults to None.
    - end_date (str, optional): The end date for the time series data. Defaults to None.
    - interval (str, optional): The interval for the time series data. Can be 'daily', 'monthly', 'weekly', 
      or intra-day intervals like '1min', '5min', etc. Defaults to None (interpreted as 'daily').

    Returns:
    - pandas.DataFrame: A DataFrame containing the requested time series data. Returns None if an error occurs.
    """

    # Load daily time series
    if interval is None or interval == 'daily':
        with SuppressPrint():
            df = openbb.crypto.load(symbol,
                                    start_date=start_date,
                                    end_date=end_date)
        data.print_dates_msg(df, start_date, end_date)
    # Load monthly data
    elif interval == 'monthly':
        with SuppressPrint():
            df = openbb.crypto.load(symbol,
                                    start_date=start_date,
                                    end_date=end_date,
                                    int=43200)
        data.print_dates_msg(df, start_date, end_date)
    # Load weekly data
    elif interval == 'weekly':
        with SuppressPrint():
            df = openbb.crypto.load(symbol,
                                    start_date=start_date,
                                    end_date=end_date,
                                    interval=10080)
        data.print_dates_msg(df, start_date, end_date)
    # Load intra-day data
    elif interval in ['1min', '5min', '15min', '30min', '60min']:
        with SuppressPrint():
            int(interval.replace('min', ''))
            df = openbb.crypto.load(symbol,
                                    start_date=start_date,
                                    end_date=end_date,
                                    interval=interval)
            data.print_dates_msg(df, start_date, end_date)
    # Handle invalid time-step ()
    else:
        print(f"Invalid time-step: '{interval}'")
        return None

    return df
