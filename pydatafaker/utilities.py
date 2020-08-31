import numpy as np
import pandas as pd


def create_date(min_year=2000, max_year=2020):
    """Create a random date.

    Parameters
    ----------
    min_year : int, optional
        The minimum possible year, by default 2000.
    max_year : int, optional
        The maximum possible year, by default 2020.

    Returns
    -------
    pandas.Timestamp
        A random date.
    """
    year = np.random.randint(min_year, max_year, size=1)[0]
    month = np.random.randint(1, 13, size=1)[0]
    if month == 2:
        max_day = 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    else:
        max_day = 30
    day = np.random.randint(1, 29, size=1)[0]
    date = pd.to_datetime("-".join([str(year), str(month).zfill(2), str(day).zfill(2)]))
    return date
