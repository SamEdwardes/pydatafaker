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

    Examples
    --------
    >>> from pydatafaker import business
    >>> business.create_vendor_table()
        vendor_id                 vendor_name  ...                   phone                       email
    0   vendor_00001                   Cross PLC  ...        140.020.8594x615   christopher58@example.org
    1   vendor_00002  Reese, Alexander and Brown  ...              3053622738       anthony47@example.net
    2   vendor_00003                 Collins LLC  ...  001-762-921-2180x55306  josephanderson@example.org
    3   vendor_00004              Newton-Salazar  ...     (316)484-7324x28092         wcastro@example.net
    4   vendor_00005                   Lee-Pratt  ...   +1-273-523-6439x95391     stephenbeck@example.org
    ..           ...                         ...  ...                     ...                         ...
    95  vendor_00096                 Jones Group  ...         +1-356-662-3508          zcline@example.org
    96  vendor_00097     Gray, Allison and Gomez  ...           (410)086-2754   sandersrobert@example.net
    97  vendor_00098                  Moreno PLC  ...      (854)754-1215x6266       johnjones@example.org
    98  vendor_00099                  Ruiz-Evans  ...       177-212-9248x3227   gregorybryant@example.org
    99  vendor_00100               Taylor-Harmon  ...            180.498.3960      maryrangel@example.com
    [100 rows x 6 columns]
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

    Examples
    --------
    >>> from pydatafaker import business
    >>> business.create_employee_table(['vendor_1', 'vendor_2'], 5)
        employee_id      employee_name vendor_id
    0  employee_00001   Matthew Sandoval  vendor_1
    1  employee_00002  Christina Holland  vendor_2
    2  employee_00003     Alice Gonzales  vendor_2
    3  employee_00004   Savannah Proctor  vendor_2
    4  employee_00005   Vanessa Hamilton  vendor_1
    5  employee_00006      Justin Holmes  vendor_2
    6  employee_00007         David Luna  vendor_2
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

    Examples
    --------
    >>> from pydatafaker import business
    >>> business.create_po_table(['vendor_1', 'vendor_2'], n=3)
        po_id vendor_id  po_amount
    0  po_00001  vendor_1     913350
    1  po_00002  vendor_2     852461
    2  po_00003  vendor_2    1355507
    3  po_00004  vendor_1    1064312
    4  po_00005  vendor_1    1017772
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

    Examples
    --------
    >>> from pydatafaker import business
    >>> po_table = business.create_po_table(['vendor_1', 'vendor_2'], n=3)
    >>> inv_summary, inv_line_item = business.create_invoice_table(po_table)
    >>> inv_summary
        invoice_id  amount invoice_date     po_id vendor_id
    0    inv_00001   87829   2010-09-12  po_00001  vendor_1
    1    inv_00002  111015   2006-11-08  po_00002  vendor_2
    2    inv_00003  113403   2013-07-01  po_00003  vendor_1
    3    inv_00004  100322   2000-01-04  po_00004  vendor_1
    4    inv_00005  127148   2014-10-27  po_00005  vendor_2
    ..         ...     ...          ...       ...       ...
    250  inv_00251   73123   2015-04-22  po_00004  vendor_1
    251  inv_00252  108463   2000-10-20  po_00004  vendor_1
    252  inv_00253   66640   2008-03-02  po_00003  vendor_1
    253  inv_00254  134062   2019-09-02  po_00002  vendor_2
    254  inv_00255  105510   2007-09-24  po_00002  vendor_2
    [255 rows x 5 columns]
    >>> inv_line_item
        invoice_id      invoice_line_id  amount    description
    0     inv_00001  line_item_000000001    3122  0-7745-2454-5
    1     inv_00001  line_item_000001972    7211  1-884097-46-4
    2     inv_00001  line_item_000002279    5460  1-80940-801-6
    3     inv_00001  line_item_000002367   10747  0-7425-2011-0
    4     inv_00001  line_item_000002491    9836  1-303-76036-3
    ...         ...                  ...     ...            ...
    5250  inv_00255  line_item_000005166    3916  0-8466-4508-4
    5251  inv_00255  line_item_000001643    5948  1-334-08325-8
    5252  inv_00255  line_item_000000734    6931  0-13-809752-6
    5253  inv_00255  line_item_000003126    5303  1-57517-108-2
    5254  inv_00255  line_item_000003778    2161  0-222-91897-7
    [5255 rows x 4 columns]
    """
    fake = Faker()
    n_pos = len(po_table["po_id"].to_list())
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
    invoice_summary["po_id"] = (
        po_table["po_id"].to_list()
        + np.random.choice(
            po_table["po_id"], replace=True, size=n_rows_inv - n_pos
        ).tolist()
    )
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

    Examples
    --------
    >>> from pydatafaker import business
    >>> biz = business.create_business()
    >>> biz.keys
    <built-in method keys of dict object at 0x000001EC7F532E40>
    >>> biz.keys()
    dict_keys(['vendor_table', 'po_table', 'invoice_summary_table', 'invoice_line_item_table', 'employee_table', 'contract_table', 'rate_sheet_table', 'timesheet_table'])
    >>> biz['vendor_table']
        vendor_id                vendor_name  ...               phone                      email
    0   vendor_00001             Byrd-Gutierrez  ...        845.182.3329    gamblekatie@example.com
    1   vendor_00002   Shaw, White and Richmond  ...  (378)573-4689x8570    cindylucero@example.org
    2   vendor_00003  Boyd, Mosley and Santiago  ...        070-378-7627       egoodwin@example.net
    3   vendor_00004            Hernandez-Klein  ...       (778)011-8623        jason05@example.com
    4   vendor_00005                  Ayers LLC  ...  (685)853-4020x9781     loriwalker@example.com
    ..           ...                        ...  ...                 ...                        ...
    95  vendor_00096  Benson, Durham and Kelley  ...       (886)807-6220  powersnatalie@example.org
    96  vendor_00097                   Hill PLC  ...       (958)223-4924     dianepayne@example.net
    97  vendor_00098                Delgado LLC  ...        278-256-0545         john97@example.net
    98  vendor_00099               Romero Group  ...       (699)578-3025    erikcarlson@example.com
    99  vendor_00100                Stevens Inc  ...          1485591460       daniel91@example.net
    [100 rows x 6 columns]
    >>> biz['employee_table']
            employee_id      employee_name     vendor_id
    0    employee_00001  Richard Robertson  vendor_00001
    1    employee_00002          Amanda Wu  vendor_00002
    2    employee_00003     Nicholas Brown  vendor_00003
    3    employee_00004        Betty Evans  vendor_00004
    4    employee_00005     Jennifer Lewis  vendor_00005
    ..              ...                ...           ...
    195  employee_00196     Madison Rivera  vendor_00094
    196  employee_00197        Denise Rose  vendor_00092
    197  employee_00198         Peter Moss  vendor_00012
    198  employee_00199     Sydney Coleman  vendor_00071
    199  employee_00200   Julie Strickland  vendor_00095
    [200 rows x 3 columns]
    >>> biz['invoice_line_item_table']
        invoice_id      invoice_line_id  amount    description
    0     inv_00001  line_item_000000001    3621  0-320-40333-5
    1     inv_00001  line_item_000004269    4494  0-437-82194-3
    2     inv_00001  line_item_000002923    4747  1-66714-426-X
    3     inv_00001  line_item_000004644    4013  0-371-59348-4
    4     inv_00001  line_item_000001550   12146  0-04-668150-7
    ...         ...                  ...     ...            ...
    5445  inv_00450  line_item_000004997    6167  0-06-558662-X
    5446  inv_00450  line_item_000000450    4039  1-118-57228-9
    5447  inv_00450  line_item_000003202   13686  1-893058-35-2
    5448  inv_00450  line_item_000003791    4145  0-906649-99-4
    5449  inv_00450  line_item_000000846    9113  1-04-617333-2
    [5450 rows x 4 columns]
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
