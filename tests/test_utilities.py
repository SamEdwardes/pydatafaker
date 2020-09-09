import pandas as pd

from pydatafaker import utilities


def test_create_date():
    x = utilities.create_date()
    assert type(x) is pd.Timestamp


def test_create_date_ranges():
    sep_1 = "2020-09-01"
    sep_2 = "2020-09-02"
    sep_3 = "2020-09-03"
    for _ in range(25):
        x = utilities.create_date(sep_1, sep_3)
        assert (
            x == pd.to_datetime(sep_1)
            or x == pd.to_datetime(sep_2)
            or x == pd.to_datetime(sep_3)
        )
