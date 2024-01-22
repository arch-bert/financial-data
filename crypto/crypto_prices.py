from utils.suppress_print import SuppressPrint
from dateutil.parser import ParserError
from openbb_terminal.sdk import openbb
from utils import data


def get_time_series(symbol, start_date=None, end_date=None, time_step=None):

    try:
        # Load daily time series
        if time_step is None or time_step == 'daily':
            with SuppressPrint():
                df = openbb.crypto.load(symbol,
                                        start_date=start_date,
                                        end_date=end_date)
            data.print_dates_msg(df, start_date, end_date)
        # Load monthly data
        elif time_step == 'monthly':
            with SuppressPrint():
                df = openbb.crypto.load(symbol,
                                        start_date=start_date,
                                        end_date=end_date,
                                        int=43200)
            data.print_dates_msg(df, start_date, end_date)
        # Load weekly data
        elif time_step == 'weekly':
            with SuppressPrint():
                df = openbb.crypto.load(symbol,
                                        start_date=start_date,
                                        end_date=end_date,
                                        interval=10080)
            data.print_dates_msg(df, start_date, end_date)
        # Load intra-day data
        elif time_step in ['1min', '5min', '15min', '30min', '60min']:
            with SuppressPrint():
                int(time_step.replace('min', ''))
                df = openbb.crypto.load(symbol,
                                        start_date=start_date,
                                        end_date=end_date,
                                        interval=time_step)
                data.print_dates_msg(df, start_date, end_date)
        # Handle invalid time-step ()
        else:
            print(f"Invalid time-step: '{time_step}'")
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
