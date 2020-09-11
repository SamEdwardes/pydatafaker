from pydatafaker import business


def test_create_business():
    x = business.create_business(n_vendors=101, n_employees=101)
    assert type(x) is dict
    assert x["vendor_table"].shape[0] == 101
    assert x["employee_table"].shape[0] == 101 + 101


def test_create_business_complete_data():
    # create business
    x = business.create_business(n_vendors=101, n_employees=101)
    vendor_table = x["vendor_table"]
    employee_table = x["employee_table"]
    po_table = x["po_table"]
    invoice_summary_table = x["invoice_summary_table"]
    invoice_line_item_table = x["invoice_line_item_table"]
    vendor_ids = vendor_table["vendor_id"].to_list()
 
    # check if vendors are complete
    # check each vendor has at least one employee
    v_ids_employee = sorted(employee_table["vendor_id"].unique().tolist())
    for i in vendor_ids:
        assert i in v_ids_employee
    # check each vendor has at least one po
    v_ids_po = sorted(po_table["vendor_id"].unique().tolist())
    for i in vendor_ids:
        assert i in v_ids_po
    # check each vendor has at least one invoice
    v_ids_inv = sorted(invoice_summary_table["vendor_id"].unique().tolist())
    for i in vendor_ids:
        assert i in v_ids_inv
    # check each vendor has at least one invoice line item
    invoice_line_item_table = invoice_line_item_table.merge(
        invoice_summary_table[["vendor_id", "invoice_id"]],
        how="left",
        on="invoice_id"
    )
    v_ids_inv_line = sorted(invoice_line_item_table["vendor_id"].unique().tolist())
    for i in vendor_ids:
        assert i in v_ids_inv_line
