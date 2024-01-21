from openbb_terminal.sdk import openbb
from utils.suppress_print import SuppressPrint
from utils import data

# TODO: error handling: ie wrong symbol


def get_time_series(symbol, start_date=None, end_date=None, time_step=None):

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

    return df
