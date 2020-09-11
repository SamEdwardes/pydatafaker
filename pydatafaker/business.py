"""
Create a business with fake data.
"""
import numpy as np
import pandas as pd
from faker import Faker

from pydatafaker.utilities import create_date


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
            "vendor_name": [fake.company() for _ in range(n)],
            "vendor_description": [fake.catch_phrase() for _ in range(n)],
            "address": [fake.address() for _ in range(n)],
            "phone": [fake.phone_number() for _ in range(n)],
            "email": [fake.safe_email() for _ in range(n)],
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
        The number of additional employees to create in excess of 1 employee
        for each vendor. By default 100.

    Returns
    -------
    pandas.DataFrame
        A dataframe containing: employee_id, employee_name, and vendor_id.
    """
    fake = Faker()
    n_vendors = len(vendor_id)
    n_rows = n + n_vendors
    x = pd.DataFrame(
        {
            "employee_id": [
                "employee_" + str(i).zfill(5) for i in range(1, n_rows + 1)
            ],
            "employee_name": [fake.name() for _ in range(n_rows)],
            "vendor_id": vendor_id
            + np.random.choice(vendor_id, replace=True, size=n).tolist(),
        }
    )
    return x


def create_po_table(vendor_id, mean_po_amount=1_000_000, sd_po_amount=250_000, n=100):
    """Create a table of fake purchase orders (PO).

    Parameters
    ----------
    vendor_id : list
        A list of vendor ids to randomly assign to employees.
    n : int, optional
        The number of additional POs to create in excess of 1 PO for each
        vendor. By default 100.
    mean_po_amount : int, optional
        Mean value for normal distribution, by default 1_000_000.
    sd_po_amount : int, optional
        Standard deviation value for normal distribution, by default 250_000.

    Returns
    -------
    pandas.DataFrame
        A dataframe containing: po_id, vendor_id, and po_amount
    """
    n_vendors = len(vendor_id)
    n_rows = n + n_vendors
    x = pd.DataFrame(
        {
            "po_id": ["po_" + str(i).zfill(5) for i in range(1, n_rows + 1)],
            "vendor_id": vendor_id
            + np.random.choice(vendor_id, replace=True, size=n).tolist(),
            "po_amount": np.abs(
                np.random.normal(mean_po_amount, sd_po_amount, size=n_rows)
            ).astype(int),
        }
    )
    return x


def create_invoice_table(
    po_table,
    mean_inv_line_amount=5_000,
    sd_inv_line_amount=4_000,
    min_date="2000-01-01",
    max_date="2020-12-31",
    n_invoice=250,
    n_line_item=5_000,
):
    """Create fake invoice and invoice line item tables.

    Parameters
    ----------
    po_table : pd.DataFrame
        The purchase order table created by create_po_table().
    mean_inv_line_amount : int, optional
        The mean value of invoice line items, by default 5_000.
    sd_inv_line_amount : int, optional
        The standard deviation of invoice line items, by default 4_000.
    min_date : str, optional
        The minimum possible date, by default '2000-01-01'.
    max_date : str, optional
        The maximum possible date, by default '2020-12-31'.
    n_invoice : int, optional
        The number of invoices to generate in excess of 1 invoice for
        each PO. By default 250.
    n_line_item : int, optional
        The number of invoice line items to generate in excess of 1 line item
        per invoice. By default 5_000.

    Returns
    -------
    (pandas.DataFrame, pandas.DataFrame)
        A tuple of two dataframes: invoice_summary and invoice_line_items.
    """
    fake = Faker()
    n_pos = len(po_table['po_id'].to_list())
    n_rows_inv = n_pos + n_invoice
    n_rows_inv_line = n_rows_inv + n_line_item
    invoice_ids = ["inv_" + str(i).zfill(5) for i in range(1, n_rows_inv + 1)]
    # invoice line items
    invoice_line_items = pd.DataFrame(
        {
            "invoice_id": invoice_ids
            + np.random.choice(invoice_ids, replace=True, size=n_line_item).tolist(),
            "invoice_line_id": [
                "line_item_" + str(i).zfill(9) for i in range(1, n_rows_inv_line + 1)
            ],
            "amount": np.abs(
                np.random.normal(
                    mean_inv_line_amount, sd_inv_line_amount, size=n_rows_inv_line
                )
            ).astype(int),
            "description": [fake.isbn10() for _ in range(n_rows_inv_line)],
        }
    )
    invoice_line_items = invoice_line_items.sort_values(by="invoice_id").reset_index(
        drop=True
    )
    # invoice summary
    invoice_summary = invoice_line_items.groupby("invoice_id")[["amount"]].sum()
    invoice_summary = invoice_summary.reset_index()
    invoice_summary["invoice_date"] = [
        create_date(min_date, max_date) for _ in range(n_rows_inv)
    ]
    invoice_summary["po_id"] = po_table['po_id'].to_list() + np.random.choice(
        po_table["po_id"], replace=True, size=n_rows_inv - n_pos
    ).tolist()
    invoice_summary = invoice_summary.merge(
        po_table[["po_id", "vendor_id"]], how="left", on="po_id"
    )
    return (invoice_summary, invoice_line_items)


def create_business(
    n_vendors=100,
    n_employees=100,
    n_pos=100,
    mean_po_amount=1_000_000,
    sd_po_amount=250_000,
    mean_inv_line_amount=5_000,
    sd_inv_line_amount=4_000,
    min_date="2000-01-01",
    max_date="2020-12-31",
    n_invoice=250,
    n_line_item=5_000,
):
    """Create an entire fake business.

    A meta function that creates many tables with related entities. A
    dictionary is returned that contains the following tables:

    - vendor_table
    - po_table
    - invoice_summary_table
    - invoice_line_item_table
    - employee_table
    - rate_sheet_table (under development)
    - contract_table (under development)
    - timesheet_table (under development)

    The tables are related to eachother in such a way that all tables can be
    combined to access different data.

    Parameters
    ----------
    n_vendors : int, optional
        The number of fake vendors to create, by default 100.
    n_employees : int, optional
        The number of additional employees to create in excess of 1 employee
        for each vendor. By default 100.
    n_pos : The number of additional POs to create in excess of 1 PO for each
        vendor. By default 100.
    mean_po_amount : int, optional
        Mean value for normal distribution, by default 1_000_000.
    sd_po_amount : int, optional
        Standard deviation value for normal distribution, by default 250_000.
    mean_inv_line_amount : int, optional
        The mean value of invoice line items, by default 5_000.
    sd_inv_line_amount : int, optional
        The standard deviation of invoice line items, by default 4_000.
    min_date : str, optional
        The minimum possible date, by default '2000-01-01'.
    max_date : str, optional
        The maximum possible date, by default '2020-12-31'.
    n_invoice : int, optional
        The number of invoices to generate in excess of 1 invoice for
        each PO. By default 250.
    n_line_item : int, optional
        The number of invoice line items to generate in excess of 1 line item
        per invoice. By default 5_000.

    Returns
    -------
    dict
        A dictionary containing related dataframes.
    """
    vendor_table = create_vendor_table(n=n_vendors)
    vendor_ids = vendor_table["vendor_id"].to_list()
    employee_table = create_employee_table(vendor_ids, n=n_employees)
    po_table = create_po_table(vendor_ids, mean_po_amount, sd_po_amount, n=n_pos)
    invoice_summary_table, invoice_line_item_table = create_invoice_table(
        po_table,
        mean_inv_line_amount,
        sd_inv_line_amount,
        min_date,
        max_date,
        n_invoice,
        n_line_item,
    )
    x = {
        "vendor_table": vendor_table,
        "po_table": po_table,
        "invoice_summary_table": invoice_summary_table,
        "invoice_line_item_table": invoice_line_item_table,
        "employee_table": employee_table,
        "contract_table": None,
        "rate_sheet_table": None,
        "timesheet_table": None,
    }
    return x
