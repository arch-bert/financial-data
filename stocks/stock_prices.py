from openbb_terminal.sdk import openbb
from utils.suppress_print import SuppressPrint

# TODO: error handling
# TODO: Print out actual start and end dates for fetched data


def get_time_series(symbol, start_date=None, end_date=None, time_step=None):

    with SuppressPrint():
        # Load daily time series
        if time_step is None or time_step == 'daily':
            df = openbb.stocks.load(symbol,
                                    start_date=start_date,
                                    end_date=end_date)

        elif time_step == 'monthly':
            df = openbb.stocks.load(symbol,
                                    start_date=start_date,
                                    end_date=end_date,
                                    monthly=True)

        elif time_step == 'weekly':
            df = openbb.stocks.load(symbol,
                                    start_date=start_date,
                                    end_date=end_date,
                                    weekly=True)

        elif time_step in ['1min', '5min', '15min', '30min', '60min']:
            int(time_step.replace('min', ''))
            df = openbb.stocks.load(symbol,
                                    start_date=start_date,
                                    end_date=end_date,
                                    interval=time_step)
    return df
