import numpy as np
import pandas as pd


def create_date(start_date="2020-01-01", end_date="2020-12-31"):
    """Create a random date.

    Parameters
    ----------
    start_date : str, optional
        The minimum possible date, by default '2020-01-01'. The format must be
        yyyy-mm-dd.
    end_date : str, optional
        The maximum possible date, by default '2020-12-31'. The format must be
        yyyy-mm-dd.

    Returns
    -------
    pandas.Timestamp
        A random date.
    """
    start_date = pd.to_datetime([start_date])
    end_date = pd.to_datetime([end_date])
    if start_date > end_date:
        raise ValueError("start_date must be before or the same as end_date")
    unix_day_0 = pd.to_datetime(["1970-01-01"])
    unix_start = (start_date - unix_day_0).days[0]
    unix_end = (end_date - unix_day_0).days[0]
    date = np.random.randint(unix_start, unix_end + 1)
    date = pd.to_datetime(date, origin="unix", unit="D")
    return date
