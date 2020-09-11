
![logo](docs/source/_static/logo_with_grey_text.png)

![test\_with\_pytest](https://github.com/SamEdwardes/pydatafaker/workflows/test_with_pytest/badge.svg)
[![Documentation
Status](https://readthedocs.org/projects/pydatafaker/badge/?version=latest)](https://pydatafaker.readthedocs.io/en/latest/?badge=latest)

PyDataFaker is a python package to create fake data with relationships
between tables. Creating fake data can be useful for many different
applications such as creating product demos or testing software.

Python already has a great package for creating fake data called Faker
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

  - **Business**: create a fake business with common ERP like tables
  - **School**: create a fake school

More entities are currently being developed. If you have any ideas of
additional entities that should be included please submit an issue here:
<https://github.com/SamEdwardes/pydatafaker/issues>.

## Table of contents

  - [Installation](#installation)
  - [Documentation](#documentation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [Credits](#credits)

## Installation

``` bash
pip install pydatafaker
```

## Documentation

Documentation can be found at
<https://pydatafaker.readthedocs.io/en/latest/index.html>. The package
is distributed through PyPi at <https://pypi.org/project/pydatafaker/>

## Usage

### Business

The business module allows you to create fake business data. Calling
`business.create_business()` will return a dictionary of related tables.

``` python
import pandas as pd
from pydatafaker import business
biz =  business.create_business()
biz.keys()
```

    ## dict_keys(['vendor_table', 'po_table', 'invoice_summary_table', 'invoice_line_item_table', 'employee_table', 'contract_table', 'rate_sheet_table', 'timesheet_table'])

Each value inside the dictionary contains a Pandas DataFrame.

``` python
biz['invoice_summary_table']
```

    ##     invoice_id  amount invoice_date     po_id     vendor_id
    ## 0    inv_00001  112392   2016-01-10  po_00003  vendor_00093
    ## 1    inv_00002  155508   2000-02-18  po_00095  vendor_00033
    ## 2    inv_00003   78362   2014-12-01  po_00001  vendor_00025
    ## 3    inv_00004  123528   2000-03-14  po_00001  vendor_00025
    ## 4    inv_00005   49888   2015-03-23  po_00081  vendor_00075
    ## ..         ...     ...          ...       ...           ...
    ## 245  inv_00246  155793   2011-11-15  po_00081  vendor_00075
    ## 246  inv_00247   95235   2009-08-12  po_00083  vendor_00088
    ## 247  inv_00248  126292   2010-05-07  po_00086  vendor_00088
    ## 248  inv_00249   96395   2010-08-05  po_00065  vendor_00036
    ## 249  inv_00250   61256   2018-04-28  po_00078  vendor_00091
    ## 
    ## [250 rows x 5 columns]

Tables can be joined together to add additional details.

``` python
invoice_summary = biz['invoice_summary_table']
vendors = biz['vendor_table']

pd.merge(invoice_summary, vendors, how='left', on='vendor_id')
```

    ##     invoice_id  amount  ...                phone                       email
    ## 0    inv_00001  112392  ...  (878)925-9060x48837        joanne31@example.net
    ## 1    inv_00002  155508  ...  (085)250-3658x57756  simpsonmatthew@example.net
    ## 2    inv_00003   78362  ...     001-060-773-3423      juliashort@example.org
    ## 3    inv_00004  123528  ...     001-060-773-3423      juliashort@example.org
    ## 4    inv_00005   49888  ...   516-622-9334x65178        andrew77@example.org
    ## ..         ...     ...  ...                  ...                         ...
    ## 245  inv_00246  155793  ...   516-622-9334x65178        andrew77@example.org
    ## 246  inv_00247   95235  ...         785-421-2374   crystalsutton@example.org
    ## 247  inv_00248  126292  ...         785-421-2374   crystalsutton@example.org
    ## 248  inv_00249   96395  ...   (126)191-5842x2835         logan03@example.org
    ## 249  inv_00250   61256  ...        (396)940-5345         gmurphy@example.com
    ## 
    ## [250 rows x 10 columns]

### School

``` python
import pandas as pd
from pydatafaker import school
skool =  school.create_school()
skool.keys()
```

    ## dict_keys(['student_table', 'teacher_table', 'room_table', 'grade_table'])

``` python
skool['student_table']
```

    ##       student_id              name  grade    teacher_id
    ## 0   student_0023   Samantha Hebert      1  teacher_0010
    ## 1   student_0024  Dustin Hernandez      1  teacher_0003
    ## 2   student_0032       Sylvia Reed      1  teacher_0010
    ## 3   student_0034          Glen Kim      1  teacher_0010
    ## 4   student_0049     Cynthia Huynh      1  teacher_0010
    ## ..           ...               ...    ...           ...
    ## 37  student_0273      Steven Scott      7  teacher_0005
    ## 38  student_0284    Julie Martinez      7  teacher_0005
    ## 39  student_0287        Sarah Ross      7  teacher_0005
    ## 40  student_0295        Jill Jones      7  teacher_0005
    ## 41  student_0299       Stacy Smith      7  teacher_0005
    ## 
    ## [300 rows x 4 columns]

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
