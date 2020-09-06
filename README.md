
# PyDataFaker

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
    ## 0    inv_00001  113523   2007-03-03  po_00054  vendor_00056
    ## 1    inv_00002  138918   2015-12-10  po_00082  vendor_00005
    ## 2    inv_00003   74733   2016-12-11  po_00056  vendor_00095
    ## 3    inv_00004   94950   2003-02-04  po_00012  vendor_00085
    ## 4    inv_00005   65429   2010-09-08  po_00060  vendor_00078
    ## ..         ...     ...          ...       ...           ...
    ## 245  inv_00246  124564   2000-05-08  po_00010  vendor_00068
    ## 246  inv_00247  108703   2013-01-15  po_00099  vendor_00072
    ## 247  inv_00248  124734   2014-12-16  po_00079  vendor_00051
    ## 248  inv_00249  100626   2016-08-02  po_00047  vendor_00052
    ## 249  inv_00250   75489   2004-10-13  po_00047  vendor_00052
    ## 
    ## [250 rows x 5 columns]

Tables can be joined together to add additional details.

``` python
invoice_summary = biz['invoice_summary_table']
vendors = biz['vendor_table']

pd.merge(invoice_summary, vendors, how='left', on='vendor_id')
```

    ##     invoice_id  amount  ...                 phone                     email
    ## 0    inv_00001  113523  ...  001-828-249-6157x408  nicholashuff@example.org
    ## 1    inv_00002  138918  ...          859.096.2158   elizabeth66@example.org
    ## 2    inv_00003   74733  ...  +1-464-465-9562x0288  sarahbennett@example.com
    ## 3    inv_00004   94950  ...      001-513-424-8491   zacharyyang@example.org
    ## 4    inv_00005   65429  ...         (482)058-1418      denise65@example.org
    ## ..         ...     ...  ...                   ...                       ...
    ## 245  inv_00246  124564  ...          195-749-4878          vmay@example.net
    ## 246  inv_00247  108703  ...  001-968-278-4877x690   brianmacias@example.org
    ## 247  inv_00248  124734  ...      730.130.8577x132       qsnyder@example.net
    ## 248  inv_00249  100626  ...         (272)217-8221       vicki33@example.org
    ## 249  inv_00250   75489  ...         (272)217-8221       vicki33@example.org
    ## 
    ## [250 rows x 10 columns]

### School

``` python
import pandas as pd
from pydatafaker import school
skool =  school.create_school()
skool.keys()
```

    ## dict_keys(['student_table', 'teacher_table', 'room_table'])

``` python
skool['student_table']
```

    ##       student_id                  name  grade    teacher_id
    ## 0   student_0001       Christopher Ray      1  teacher_0011
    ## 1   student_0002          Henry Jacobs      1  teacher_0011
    ## 2   student_0004           Brenda Mays      1  teacher_0010
    ## 3   student_0019          Laura Thomas      1  teacher_0011
    ## 4   student_0022         Philip Taylor      1  teacher_0010
    ## ..           ...                   ...    ...           ...
    ## 33  student_0263        Wesley Johnson      7  teacher_0012
    ## 34  student_0266        Jennifer Reyes      7  teacher_0012
    ## 35  student_0276    Abigail Cunningham      7  teacher_0016
    ## 36  student_0283  Christina Fitzgerald      7  teacher_0012
    ## 37  student_0288       Mr. Walter Rios      7  teacher_0012
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
