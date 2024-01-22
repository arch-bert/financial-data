from openbb_terminal.sdk import openbb
from utils.suppress_print import SuppressPrint
from utils import data

# TODO: error handling: ie wrong symbol


def get_time_series(symbol, start_date=None, end_date=None, time_step=None):
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
    time_step (str, optional): The time step or interval for the data. Valid options include 'daily', 'weekly', 
        'monthly', '1min', '5min', '15min', '30min', '60min'. If None or 'daily', daily data is fetched. Default is None.

    Returns:
    pd.DataFrame: A DataFrame containing the time series data for the specified stock symbol.

    Notes:
    - The function suppresses print statements from the OpenBB Terminal's load function using the SuppressPrint context manager.
    - It also prints messages about the availability of data for the requested dates using the 'print_dates_msg' function.
    """

    try:
        # Load daily time series
        if time_step is None or time_step == 'daily':
            with SuppressPrint():
                df = openbb.stocks.load(symbol,
                                        start_date=start_date,
                                        end_date=end_date)
            data.print_dates_msg(df, start_date, end_date)

        elif time_step == 'monthly':
            with SuppressPrint():
                df = openbb.stocks.load(symbol,
                                        start_date=start_date,
                                        end_date=end_date,
                                        monthly=True)
            data.print_dates_msg(df, start_date, end_date)

        elif time_step == 'weekly':
            with SuppressPrint():
                df = openbb.stocks.load(symbol,
                                        start_date=start_date,
                                        end_date=end_date,
                                        weekly=True)
            data.print_dates_msg(df, start_date, end_date)

        elif time_step in ['1min', '5min', '15min', '30min', '60min']:
            with SuppressPrint():
                int(time_step.replace('min', ''))
                df = openbb.stocks.load(symbol,
                                        start_date=start_date,
                                        end_date=end_date,
                                        interval=time_step)
                data.print_dates_msg(df, start_date, end_date)

    # Handle invalid symbol error
    except IndexError:
        print(f'Invalid symbol: {symbol}')
        return None

    return df
