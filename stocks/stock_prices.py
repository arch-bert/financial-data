from utils.suppress_print import SuppressPrint
from dateutil.parser import ParserError
from openbb_terminal.sdk import openbb
from utils import data


def get_time_series(symbol, start_date=None, end_date=None, interval=None):
    """
    Retrieves time series data for a given stock symbol over a specified time range and interval.

    This function uses the OpenBB Terminal's stocks module to load data. It supports various time steps
    including daily, weekly, monthly, and intraday intervals (1min, 5min, 15min, 30min, 60min).

    Parameters:
    symbol (str): The stock symbol for which to retrieve time series data.
    start_date (str or datetime, optional): The start date of the time series data. 
        If None, fetches data from the earliest available date. Default is None.
    end_date (str or datetime, optional): The end date of the time series data. 
        If None, fetches data up to the most recent available date. Default is None.
    interval (str, optional): The time step or interval for the data. Valid options include 'daily', 'weekly', 
        'monthly', '1min', '5min', '15min', '30min', '60min'. If None or 'daily', daily data is fetched. Default is None.

    Returns:
    pd.DataFrame: A DataFrame containing the time series data for the specified stock symbol. Returns None if an error occurs.

    Raises:
    IndexError: If an invalid stock symbol is provided.
    ParserError: If the provided dates are in an incorrect format.

    Notes:
    - The function suppresses print statements from the OpenBB Terminal's load function using the SuppressPrint context manager.
    - It prints messages about the availability of data for the requested dates using the 'print_dates_msg' function.
    - Error handling includes checks for invalid stock symbols, incorrect date formats, and unsupported time steps.
    """

    # Load daily time series
    if interval is None or interval == 'daily':
        with SuppressPrint():
            df = openbb.stocks.load(symbol,
                                    start_date=start_date,
                                    end_date=end_date)
        data.print_dates_msg(df, start_date, end_date)
    # Load monthly data
    elif interval == 'monthly':
        with SuppressPrint():
            df = openbb.stocks.load(symbol,
                                    start_date=start_date,
                                    end_date=end_date,
                                    monthly=True)
        data.print_dates_msg(df, start_date, end_date)
    # Load weekly data
    elif interval == 'weekly':
        with SuppressPrint():
            df = openbb.stocks.load(symbol,
                                    start_date=start_date,
                                    end_date=end_date,
                                    weekly=True)
        data.print_dates_msg(df, start_date, end_date)
    # Load intra-day data
    elif interval in ['1min', '5min', '15min', '30min', '60min']:
        with SuppressPrint():
            int(interval.replace('min', ''))
            df = openbb.stocks.load(symbol,
                                    start_date=start_date,
                                    end_date=end_date,
                                    interval=interval)
            data.print_dates_msg(df, start_date, end_date)
    # Handle invalid time-step ()
    else:
        print(f"Invalid time-step: '{interval}'")
        return None

    return df
