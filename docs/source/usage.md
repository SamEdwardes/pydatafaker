
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
biz['invoice_summary_table']
```

    ##     invoice_id  amount invoice_date     po_id     vendor_id
    ## 0    inv_00001   57187   2012-07-05  po_00060  vendor_00024
    ## 1    inv_00002  107219   2008-09-08  po_00053  vendor_00056
    ## 2    inv_00003  180758   2000-12-05  po_00056  vendor_00074
    ## 3    inv_00004   93168   2006-01-13  po_00070  vendor_00099
    ## 4    inv_00005   96457   2004-03-11  po_00032  vendor_00084
    ## ..         ...     ...          ...       ...           ...
    ## 245  inv_00246   90604   2006-10-01  po_00058  vendor_00049
    ## 246  inv_00247  112368   2018-02-02  po_00011  vendor_00083
    ## 247  inv_00248   99706   2019-05-14  po_00051  vendor_00026
    ## 248  inv_00249  152691   2016-08-27  po_00025  vendor_00093
    ## 249  inv_00250  139055   2000-02-19  po_00096  vendor_00079
    ## 
    ## [250 rows x 5 columns]

Tables can be joined together to add additional details.

``` python
invoice_summary = biz['invoice_summary_table']
vendors = biz['vendor_table']

pd.merge(invoice_summary, vendors, how='left', on='vendor_id')
```

    ##     invoice_id  amount  ...                  phone                     email
    ## 0    inv_00001   57187  ...          (614)621-1192   mcgeeaustin@example.org
    ## 1    inv_00002  107219  ...           530-689-7334     beverly63@example.com
    ## 2    inv_00003  180758  ...  +1-033-005-7309x46881        psmith@example.org
    ## 3    inv_00004   93168  ...           363-359-0031       kiara58@example.com
    ## 4    inv_00005   96457  ...        +1-905-366-5398    jeremiah08@example.org
    ## ..         ...     ...  ...                    ...                       ...
    ## 245  inv_00246   90604  ...       611.749.2423x476      aballard@example.com
    ## 246  inv_00247  112368  ...     (435)514-7431x6667     bwilliams@example.com
    ## 247  inv_00248   99706  ...           848-481-0987      oschmitt@example.net
    ## 248  inv_00249  152691  ...           782-802-3691        cole11@example.org
    ## 249  inv_00250  139055  ...      (106)670-7849x375  johnsonkelly@example.org
    ## 
    ## [250 rows x 10 columns]

## School

The school module allows you to generate fake school data

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

    ##       student_id                name  grade    teacher_id
    ## 0   student_0001  Jonathan Underwood      1  teacher_0002
    ## 1   student_0005    Tiffany Stafford      1  teacher_0006
    ## 2   student_0006         Alan Burton      1  teacher_0002
    ## 3   student_0007          David Ward      1  teacher_0006
    ## 4   student_0024     Michael Huffman      1  teacher_0002
    ## ..           ...                 ...    ...           ...
    ## 40  student_0275           Cory Gill      7  teacher_0011
    ## 41  student_0278       Robert Ramsey      7  teacher_0003
    ## 42  student_0291       Douglas Watts      7  teacher_0012
    ## 43  student_0293        Joseph Banks      7  teacher_0003
    ## 44  student_0294        Joan Barnett      7  teacher_0011
    ## 
    ## [300 rows x 4 columns]

``` python
skool['teacher_table']
```

    ##       teacher_id                name  grade   room_id
    ## 0   teacher_0001         Dana Watson      3  room_014
    ## 1   teacher_0002         Julie Moore      1  room_006
    ## 2   teacher_0003       Marissa Young      7  room_010
    ## 3   teacher_0004  Michael Williamson      2  room_012
    ## 4   teacher_0005     Michelle Palmer      4  room_009
    ## 5   teacher_0006     Stacy Rodriguez      1  room_011
    ## 6   teacher_0007     Michael Griffin      2  room_001
    ## 7   teacher_0008      Michael Grimes      6  room_005
    ## 8   teacher_0009        Erin Russell      5  room_015
    ## 9   teacher_0010         Dylan Blake      2  room_008
    ## 10  teacher_0011           Fred Rowe      7  room_016
    ## 11  teacher_0012   Christine Bradley      7  room_003
    ## 12  teacher_0013         Marc Graves      6  room_004
    ## 13  teacher_0014       Timothy Petty      3  room_002
    ## 14  teacher_0015      Allison Glover      5  room_007
    ## 15  teacher_0016      Jackson Mooney      4  room_013
    ## 16  teacher_0017         Cathy Gross      4  room_017

``` python
skool['room_table']
```

    ##      room_id  smartboard  sink  square_footage
    ## 0   room_001           0     0            1120
    ## 1   room_002           0     1             737
    ## 2   room_003           0     1            1331
    ## 3   room_004           0     1            1325
    ## 4   room_005           0     1            1020
    ## 5   room_006           0     1             825
    ## 6   room_007           0     1             764
    ## 7   room_008           1     0            1035
    ## 8   room_009           0     1             884
    ## 9   room_010           1     0            1127
    ## 10  room_011           1     1             862
    ## 11  room_012           0     0            1316
    ## 12  room_013           1     1             830
    ## 13  room_014           0     1            1009
    ## 14  room_015           0     1             787
    ## 15  room_016           0     1             480
    ## 16  room_017           0     1             923
