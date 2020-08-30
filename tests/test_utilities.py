from pydatafaker import utilities
import pandas as pd


def test_create_date():
    x = utilities.create_date()
    assert type(x) is pd.Timestamp
    
    
