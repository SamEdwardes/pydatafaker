from pydatafaker import business


def test_create_business():
    x = business.create_business(n_vendors=101, n_employees=101)
    assert type(x) is dict
    assert x["vendor_table"].shape[0] == 101
    assert x["employee_table"].shape[0] == 101
