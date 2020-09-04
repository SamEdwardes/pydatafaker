
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

Documentation can be found at
<https://pydatafaker.readthedocs.io/en/latest/index.html>.

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
    ## 0    inv_00001   85313   2006-05-18  po_00074  vendor_00020
    ## 1    inv_00002  102511   2010-03-19  po_00017  vendor_00048
    ## 2    inv_00003  116998   2004-04-04  po_00013  vendor_00006
    ## 3    inv_00004   91595   2010-03-05  po_00023  vendor_00003
    ## 4    inv_00005  127056   2014-05-13  po_00060  vendor_00028
    ## ..         ...     ...          ...       ...           ...
    ## 245  inv_00246   54936   2018-11-09  po_00071  vendor_00015
    ## 246  inv_00247   97616   2004-03-25  po_00071  vendor_00015
    ## 247  inv_00248   98365   2000-09-04  po_00064  vendor_00010
    ## 248  inv_00249   74361   2005-09-02  po_00052  vendor_00032
    ## 249  inv_00250   68888   2008-07-07  po_00073  vendor_00097
    ## 
    ## [250 rows x 5 columns]

Tables can be joined together to add additional details.

``` python
invoice_summary = biz['invoice_summary_table']
vendors = biz['vendor_table']

pd.merge(invoice_summary, vendors, how='left', on='vendor_id')
```

    ##     invoice_id  amount  ...                   phone                       email
    ## 0    inv_00001   85313  ...           (919)472-5788        daniel91@example.com
    ## 1    inv_00002  102511  ...       (178)697-5211x058    seancastillo@example.org
    ## 2    inv_00003  116998  ...            932.430.6920     mooreamanda@example.org
    ## 3    inv_00004   91595  ...        958-198-9444x355      samantha22@example.com
    ## 4    inv_00005  127056  ...  001-566-535-4000x26384     frankbarron@example.com
    ## ..         ...     ...  ...                     ...                         ...
    ## 245  inv_00246   54936  ...       135-151-8494x2791        marvin72@example.org
    ## 246  inv_00247   97616  ...       135-151-8494x2791        marvin72@example.org
    ## 247  inv_00248   98365  ...            642-833-5079  dianahernandez@example.net
    ## 248  inv_00249   74361  ...       (794)308-1258x383     billyvaldez@example.net
    ## 249  inv_00250   68888  ...   001-291-455-4032x9171    adamsjasmine@example.com
    ## 
    ## [250 rows x 10 columns]

## Contributing

Please see [docs/source/contributing.rst](docs/source/contributing.rst).

## Credits

Developed by:

  - Sam Edwardes

Logo:

  - Icon made by [Freepik](https://www.flaticon.com/authors/freepik)
    from [www.flaticon.com](https://www.flaticon.com/)
  - Front from
    [fontmeme.com/retro-fonts/](https://fontmeme.com/retro-fonts/)
  - Logo generated using [logomakr.com](logomakr.com/7scB4)
