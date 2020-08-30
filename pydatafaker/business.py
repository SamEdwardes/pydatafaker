import numpy as np
import pandas as pd
from faker import Faker


def create_vendor_table(n=100):
    """Create a table of fake vendors.

    Parameters
    ----------
    n : int, optional
        The number of vendors to create, by default 100.

    Returns
    -------
    pandas.DataFrame
        A dataframe containing: vendor_id, vendor_name, and vendor_address.
    """
    fake = Faker()
    x = pd.DataFrame(
        {
            "vendor_id": ["vendor_" + str(i).zfill(5) for i in range(1, n + 1)],
            "vendor_name": ["vendor_" + str(i).zfill(5) for i in range(1, n + 1)],
            "address": [fake.address() for _ in range(n)],
        }
    )
    return x


def create_employee_table(vendor_id, n=100):
    """Create a table of fake employees.

    Parameters
    ----------
    vendor_id : list
        A list of vendor ids to randomly assign to employees.
    n : int, optional
        The number of employees to create, by default 100.

    Returns
    -------
    pandas.DataFrame
        A dataframe containing: employee_id, employee_name, and vendor_id.
    """
    fake = Faker()
    x = pd.DataFrame(
        {
            "employee_id": ["vendor_" + str(i).zfill(5) for i in range(1, n + 1)],
            "employee_name": [fake.name() for _ in range(n)],
            "vendor_id": np.random.choice(vendor_id, replace=True, size=n),
        }
    )
    return x


def create_business(n_vendors=100, n_employees=100):
    """Create an entire fake business.
    
    A meta function that creates many tables with related entities.

    Parameters
    ----------
    n_vendors : int, optional
        The number of fake vendors to create, by default 100
    n_employees : int, optional
        The number of fake employees to create, by default 100

    Returns
    -------
    dict
        A dictionary containing related dataframes. Dictionary includes: 
        vendor_table, and employee_table.
    """
    vendor_table = create_vendor_table(n=n_vendors)
    employee_table = create_employee_table(vendor_table["vendor_id"], n=n_employees)
    x = {"vendor_table": vendor_table, "employee_table": employee_table}
    return x
