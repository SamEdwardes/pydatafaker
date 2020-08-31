
# pydatafaker

A python package to create fake data with relationships between tables.

Creating fake data can be useful for many different applications. Python
already has a great package for creating fake data called Faker
<https://faker.readthedocs.io/en/master/>. Faker is great for creating
individual fake units of data, but it can be time consuming to create
more complicated fake data that is actually related to one another.

Imagine you are developing a new enterprise resource planning (ERP)
software to challenge SAP. You may need to create some fake data to test
your application. You will need an invoice table, a vendor listing,
purchase order table, and more. PyDataFaker allows your to quickly
create these tables and generates relationships between them\!

PyDataFaker is currently under development. At this time it is possible
to create the following entities:

  - Business: create a fake business with common ERP like tables

More entities are currently being developed. If you have any ideas of
additional entities that should be included please submit an issue here:
<https://github.com/SamEdwardes/pydatafaker/issues>.

## Table of contents

  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [Credits](#credits)
  - [Reminders for developers](#reminders-for-developers)

## Installation

``` bash
pip install pydatafaker
```

## Usage

### Business

Generate fake business data that could be used to populate an ERP tool.

``` python
import pandas as pd
from pydatafaker import business
biz =  business.create_business()
```

`business.create_business()` returns a dictionary containing all of the
related tables.

``` python
biz.keys()
```

    ## dict_keys(['vendor_table', 'po_table', 'invoice_summary_table', 'invoice_line_item_table', 'employee_table', 'contract_table', 'rate_sheet_table', 'timesheet_table'])

Each value inside the dictionary contains a Pandas DataFrame.

``` python
biz['invoice_summary_table']
```

    ##     invoice_id  amount invoice_date     po_id     vendor_id
    ## 0    inv_00001  136656   2001-07-17  po_00097  vendor_00026
    ## 1    inv_00002   78312   2005-11-09  po_00009  vendor_00095
    ## 2    inv_00003   69358   2011-09-18  po_00077  vendor_00056
    ## 3    inv_00004  100768   2014-11-27  po_00032  vendor_00020
    ## 4    inv_00005  102143   2005-12-22  po_00099  vendor_00030
    ## ..         ...     ...          ...       ...           ...
    ## 245  inv_00246   97982   2005-05-24  po_00080  vendor_00081
    ## 246  inv_00247  104825   2016-09-07  po_00044  vendor_00009
    ## 247  inv_00248   74859   2006-12-08  po_00051  vendor_00090
    ## 248  inv_00249  120717   2018-12-02  po_00014  vendor_00015
    ## 249  inv_00250   86237   2006-01-13  po_00087  vendor_00077
    ## 
    ## [250 rows x 5 columns]

Tables can be joined together to add additional details.

``` python
invoice_summary = biz['invoice_summary_table']
vendors = biz['vendor_table']

pd.merge(invoice_summary, vendors, how='left', on='vendor_id')
```

    ##     invoice_id  amount  ...                  phone                     email
    ## 0    inv_00001  136656  ...     (977)744-3104x3154      alyssa30@example.net
    ## 1    inv_00002   78312  ...      (746)189-5837x622  joshuaromero@example.org
    ## 2    inv_00003   69358  ...   +1-181-492-1753x1569    dianeblack@example.org
    ## 3    inv_00004  100768  ...      (087)855-3596x448  johnroberson@example.com
    ## 4    inv_00005  102143  ...  001-921-594-2777x9395        ujones@example.com
    ## ..         ...     ...  ...                    ...                       ...
    ## 245  inv_00246   97982  ...           086-262-1268     lewislisa@example.net
    ## 246  inv_00247  104825  ...           437-043-3207   frankcarrie@example.net
    ## 247  inv_00248   74859  ...       361-768-8001x905    zvelasquez@example.com
    ## 248  inv_00249  120717  ...             2627798762     huffmolly@example.org
    ## 249  inv_00250   86237  ...             1910864834   aprilherman@example.org
    ## 
    ## [250 rows x 10 columns]

## Contributing

Please see [CONTRIBUTING.rst](CONTRIBUTING.rst).

## Credits

Developed by Sam Edwardes.

## Reminders for developers

Helpful reminders for PyDataFaker developers

### Updating the documentation

``` bash
poetry run sphinx-apidoc -f -o docs/source pydatafaker
cd docs
poetry run make html
```
