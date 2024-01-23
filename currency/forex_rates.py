from utils.suppress_print import SuppressPrint
from dateutil.parser import ParserError
from openbb_terminal.sdk import openbb
from utils import data


def get_time_series(symbol, start_date=None, end_date=None, interval=None):

    # Split forex pair into two arguments
    from_symbol, to_symbol = symbol.split('/')

    try:
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

    # Handle invalid symbol error
    except IndexError:
        print(f"Invalid symbol: '{symbol}'")
        return None

    # Handle invalid date error
    except ParserError:
        print(f"Invalid date format")
        return None

    return df
