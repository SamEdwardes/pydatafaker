
# PyDataFaker

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
  - [Documentation](#documentation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [Credits](#credits)
  - [Reminders for developers](#reminders-for-developers)

## Installation

``` bash
pip install pydatafaker
```

## Documentation

Documentation can be found on…

> TODO: update read the docs

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
    ## 0    inv_00001   97031   2010-08-07  po_00057  vendor_00036
    ## 1    inv_00002  109332   2002-07-01  po_00021  vendor_00011
    ## 2    inv_00003   91668   2018-06-14  po_00044  vendor_00024
    ## 3    inv_00004  108011   2008-10-18  po_00076  vendor_00058
    ## 4    inv_00005  110817   2019-02-04  po_00085  vendor_00038
    ## ..         ...     ...          ...       ...           ...
    ## 245  inv_00246  108461   2000-02-06  po_00035  vendor_00004
    ## 246  inv_00247   80117   2019-11-05  po_00025  vendor_00069
    ## 247  inv_00248   93032   2009-07-19  po_00084  vendor_00085
    ## 248  inv_00249  115524   2008-11-04  po_00068  vendor_00073
    ## 249  inv_00250  126293   2002-09-15  po_00059  vendor_00090
    ## 
    ## [250 rows x 5 columns]

Tables can be joined together to add additional details.

``` python
invoice_summary = biz['invoice_summary_table']
vendors = biz['vendor_table']

pd.merge(invoice_summary, vendors, how='left', on='vendor_id')
```

    ##     invoice_id  amount  ...                   phone                        email
    ## 0    inv_00001   97031  ...         +1-872-617-0969         thomas39@example.com
    ## 1    inv_00002  109332  ...        599-991-9214x966           gsmith@example.org
    ## 2    inv_00003   91668  ...    001-734-627-6973x265      dannyhoward@example.com
    ## 3    inv_00004  108011  ...        025-796-1061x564    marshallkathy@example.org
    ## 4    inv_00005  110817  ...        579-689-9896x352         vdaniels@example.net
    ## ..         ...     ...  ...                     ...                          ...
    ## 245  inv_00246  108461  ...       191.429.0233x9234    laurensanders@example.org
    ## 246  inv_00247   80117  ...      241.033.2329x22589    hensonwilliam@example.com
    ## 247  inv_00248   93032  ...            252-370-5255  cochranbrittany@example.org
    ## 248  inv_00249  115524  ...  001-995-279-0968x92447        gregory39@example.net
    ## 249  inv_00250  126293  ...       189-989-1659x6577            vgill@example.org
    ## 
    ## [250 rows x 10 columns]

## Contributing

Please see [docs/source/contributing.rst](docs/source/contributing.rst).

## Credits

Developed by Sam Edwardes.
