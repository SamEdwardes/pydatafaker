
# Usage

## Installation

To Install please run:

``` bash
pip intsall pydatafaker
```

## Business

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
biz["vendor_table"]
```

    ##        vendor_id  ...                       email
    ## 0   vendor_00001  ...        howard20@example.com
    ## 1   vendor_00002  ...     deborahneal@example.com
    ## 2   vendor_00003  ...   gwendolynlong@example.com
    ## 3   vendor_00004  ...  johnstonsteven@example.org
    ## 4   vendor_00005  ...       brandon34@example.com
    ## ..           ...  ...                         ...
    ## 95  vendor_00096  ...         annaorr@example.net
    ## 96  vendor_00097  ...           nking@example.com
    ## 97  vendor_00098  ...    georgehinton@example.net
    ## 98  vendor_00099  ...          qhaley@example.com
    ## 99  vendor_00100  ...         amydean@example.com
    ## 
    ## [100 rows x 6 columns]

``` python
biz["employee_table"]
```

    ##         employee_id     employee_name     vendor_id
    ## 0    employee_00001    Nancy Copeland  vendor_00001
    ## 1    employee_00002    James Martinez  vendor_00002
    ## 2    employee_00003    Susan Reynolds  vendor_00003
    ## 3    employee_00004  Angela Davenport  vendor_00004
    ## 4    employee_00005    Leslie Shaffer  vendor_00005
    ## ..              ...               ...           ...
    ## 195  employee_00196    Tasha Thornton  vendor_00045
    ## 196  employee_00197      Stephen Carr  vendor_00087
    ## 197  employee_00198      Daniel Smith  vendor_00066
    ## 198  employee_00199        Toni Mccoy  vendor_00071
    ## 199  employee_00200       Jenny Irwin  vendor_00017
    ## 
    ## [200 rows x 3 columns]

``` python
biz["po_table"]
```

    ##         po_id     vendor_id  po_amount
    ## 0    po_00001  vendor_00001    1044568
    ## 1    po_00002  vendor_00002     931639
    ## 2    po_00003  vendor_00003     853806
    ## 3    po_00004  vendor_00004     959485
    ## 4    po_00005  vendor_00005    1007129
    ## ..        ...           ...        ...
    ## 195  po_00196  vendor_00005     900178
    ## 196  po_00197  vendor_00030     651345
    ## 197  po_00198  vendor_00005     872324
    ## 198  po_00199  vendor_00068    1110415
    ## 199  po_00200  vendor_00049     945426
    ## 
    ## [200 rows x 3 columns]

``` python
biz["invoice_summary_table"]
```

    ##     invoice_id  amount invoice_date     po_id     vendor_id
    ## 0    inv_00001   51469   2010-06-09  po_00001  vendor_00001
    ## 1    inv_00002   96800   2018-11-28  po_00002  vendor_00002
    ## 2    inv_00003   50245   2013-06-04  po_00003  vendor_00003
    ## 3    inv_00004   52919   2015-11-25  po_00004  vendor_00004
    ## 4    inv_00005   76873   2017-02-07  po_00005  vendor_00005
    ## ..         ...     ...          ...       ...           ...
    ## 445  inv_00446   74342   2017-07-28  po_00054  vendor_00054
    ## 446  inv_00447   49413   2008-06-01  po_00092  vendor_00092
    ## 447  inv_00448   52490   2001-02-07  po_00133  vendor_00090
    ## 448  inv_00449   85486   2018-04-09  po_00062  vendor_00062
    ## 449  inv_00450   81208   2011-03-07  po_00095  vendor_00095
    ## 
    ## [450 rows x 5 columns]

``` python
biz["invoice_line_item_table"]
```

    ##      invoice_id      invoice_line_id  amount    description
    ## 0     inv_00001  line_item_000000001    5255  0-12-459790-4
    ## 1     inv_00001  line_item_000001204    4449  0-422-99512-6
    ## 2     inv_00001  line_item_000000734    3179  1-109-53494-9
    ## 3     inv_00001  line_item_000001170    3450  1-964128-06-4
    ## 4     inv_00001  line_item_000002718    6569  0-7897-3841-4
    ## ...         ...                  ...     ...            ...
    ## 5445  inv_00450  line_item_000004902    8518  1-958488-62-3
    ## 5446  inv_00450  line_item_000002125    1533  0-7108-5370-X
    ## 5447  inv_00450  line_item_000003353    9214  1-75708-639-0
    ## 5448  inv_00450  line_item_000003692     988  0-19-948511-9
    ## 5449  inv_00450  line_item_000002655    8533  1-118-87482-X
    ## 
    ## [5450 rows x 4 columns]

Tables can be joined together to add additional details.

``` python
invoice_summary = biz['invoice_summary_table']
vendors = biz['vendor_table']

pd.merge(invoice_summary, vendors, how='left', on='vendor_id')
```

    ##     invoice_id  amount  ...                  phone                       email
    ## 0    inv_00001   51469  ...       048-394-1093x364        howard20@example.com
    ## 1    inv_00002   96800  ...    (142)172-7660x13994     deborahneal@example.com
    ## 2    inv_00003   50245  ...      (005)543-4969x946   gwendolynlong@example.com
    ## 3    inv_00004   52919  ...        +1-653-464-9711  johnstonsteven@example.org
    ## 4    inv_00005   76873  ...      (536)279-6524x003       brandon34@example.com
    ## ..         ...     ...  ...                    ...                         ...
    ## 445  inv_00446   74342  ...  +1-040-165-0235x97604         helen91@example.com
    ## 446  inv_00447   49413  ...    (778)854-7679x16397           bbeck@example.org
    ## 447  inv_00448   52490  ...             0025585349      youngmisty@example.net
    ## 448  inv_00449   85486  ...   +1-890-953-5903x5845    mullinsapril@example.net
    ## 449  inv_00450   81208  ...             4709395593          wlewis@example.net
    ## 
    ## [450 rows x 10 columns]

## School

The school module allows you to generate fake school data

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

    ##       student_id                name  grade    teacher_id
    ## 0   student_0005  Stephanie Franklin      1  teacher_0003
    ## 1   student_0012       Amanda Jensen      1  teacher_0008
    ## 2   student_0013     Alexandra Smith      1  teacher_0003
    ## 3   student_0023     Madison Sanchez      1  teacher_0008
    ## 4   student_0027       Justin Golden      1  teacher_0003
    ## ..           ...                 ...    ...           ...
    ## 41  student_0270      Andrew Schmidt      7  teacher_0015
    ## 42  student_0281          John Brown      7  teacher_0005
    ## 43  student_0289    Elizabeth Martin      7  teacher_0012
    ## 44  student_0294      Michelle Miles      7  teacher_0015
    ## 45  student_0296    Austin Daugherty      7  teacher_0005
    ## 
    ## [300 rows x 4 columns]

``` python
skool['teacher_table']
```

    ##       teacher_id              name  grade   room_id
    ## 0   teacher_0001        Kevin Long      3  room_008
    ## 1   teacher_0002        Don Turner      6  room_015
    ## 2   teacher_0003     Meghan Bailey      1  room_004
    ## 3   teacher_0004       Austin Cobb      5  room_001
    ## 4   teacher_0005     Grant Herrera      7  room_007
    ## 5   teacher_0006     Erin Robinson      2  room_006
    ## 6   teacher_0007     Thomas Hunter      5  room_012
    ## 7   teacher_0008   Danielle Obrien      1  room_009
    ## 8   teacher_0009  Jeffrey Mcmillan      2  room_011
    ## 9   teacher_0010       Louis Baker      6  room_014
    ## 10  teacher_0011        Kevin Hall      4  room_003
    ## 11  teacher_0012     Richard Perez      7  room_005
    ## 12  teacher_0013    Mrs. Mary Lutz      4  room_010
    ## 13  teacher_0014       Joseph West      3  room_002
    ## 14  teacher_0015  Phillip Crawford      7  room_013
    ## 15  teacher_0016    David Williams      6  room_016

``` python
skool['room_table']
```

    ##      room_id  smartboard  sink  square_footage
    ## 0   room_001           1     0            1042
    ## 1   room_002           1     0             961
    ## 2   room_003           1     1            1183
    ## 3   room_004           0     1             893
    ## 4   room_005           1     0            1080
    ## 5   room_006           1     1             742
    ## 6   room_007           1     0             793
    ## 7   room_008           1     1             806
    ## 8   room_009           0     0             941
    ## 9   room_010           1     0            1230
    ## 10  room_011           1     1             833
    ## 11  room_012           1     1            1073
    ## 12  room_013           0     0            1147
    ## 13  room_014           1     0            1365
    ## 14  room_015           0     0            1259
    ## 15  room_016           1     0            1075

``` python
skool['grade_table']
```

    ##         student_id  test_score       date
    ## 0     student_0005    0.570712 2021-02-25
    ## 1     student_0005    0.827224 2020-10-15
    ## 2     student_0005    0.979315 2021-01-06
    ## 3     student_0005    0.916443 2020-12-23
    ## 4     student_0005    1.000000 2021-07-26
    ## ...            ...         ...        ...
    ## 2995  student_0296    0.943931 2021-01-14
    ## 2996  student_0296    0.656949 2021-07-03
    ## 2997  student_0296    0.877827 2021-05-27
    ## 2998  student_0296    0.835894 2020-12-03
    ## 2999  student_0296    0.897528 2020-12-12
    ## 
    ## [3000 rows x 3 columns]
