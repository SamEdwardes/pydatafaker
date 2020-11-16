# Usage

## Installation

To Install please run:

```bash
pip intsall pydatafaker
```

## Business

The business module allows you to create fake business data. Calling `business.create_business()` will return a dictionary of related tables.


```python
import pandas as pd
from pydatafaker import business
biz =  business.create_business()
biz.keys()
```




    dict_keys(['vendor_table', 'po_table', 'invoice_summary_table', 'invoice_line_item_table', 'employee_table', 'contract_table', 'rate_sheet_table', 'timesheet_table'])



Each value inside the dictionary contains a Pandas DataFrame.


```python
biz["vendor_table"]
biz["employee_table"]
biz["po_table"]
biz["invoice_summary_table"]
biz["invoice_line_item_table"]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>invoice_id</th>
      <th>invoice_line_id</th>
      <th>amount</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>inv_00001</td>
      <td>line_item_000000001</td>
      <td>4404</td>
      <td>0-7299-7353-0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>inv_00001</td>
      <td>line_item_000002781</td>
      <td>1233</td>
      <td>0-8184-1802-8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>inv_00001</td>
      <td>line_item_000004837</td>
      <td>5056</td>
      <td>1-4642-5447-8</td>
    </tr>
    <tr>
      <th>3</th>
      <td>inv_00001</td>
      <td>line_item_000004797</td>
      <td>5253</td>
      <td>1-175-64411-0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>inv_00001</td>
      <td>line_item_000000947</td>
      <td>1792</td>
      <td>1-956222-62-6</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5445</th>
      <td>inv_00450</td>
      <td>line_item_000000707</td>
      <td>4198</td>
      <td>0-603-62234-8</td>
    </tr>
    <tr>
      <th>5446</th>
      <td>inv_00450</td>
      <td>line_item_000003163</td>
      <td>4131</td>
      <td>1-06-101759-1</td>
    </tr>
    <tr>
      <th>5447</th>
      <td>inv_00450</td>
      <td>line_item_000003874</td>
      <td>5193</td>
      <td>0-482-36167-0</td>
    </tr>
    <tr>
      <th>5448</th>
      <td>inv_00450</td>
      <td>line_item_000005441</td>
      <td>4189</td>
      <td>1-03-258645-1</td>
    </tr>
    <tr>
      <th>5449</th>
      <td>inv_00450</td>
      <td>line_item_000000915</td>
      <td>3398</td>
      <td>0-03-148841-2</td>
    </tr>
  </tbody>
</table>
<p>5450 rows × 4 columns</p>
</div>



Tables can be joined together to add additional details.


```python
invoice_summary = biz['invoice_summary_table']
vendors = biz['vendor_table']

pd.merge(invoice_summary, vendors, how='left', on='vendor_id')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>invoice_id</th>
      <th>amount</th>
      <th>invoice_date</th>
      <th>po_id</th>
      <th>vendor_id</th>
      <th>vendor_name</th>
      <th>vendor_description</th>
      <th>address</th>
      <th>phone</th>
      <th>email</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>inv_00001</td>
      <td>50384</td>
      <td>2014-01-22</td>
      <td>po_00001</td>
      <td>vendor_00001</td>
      <td>Duran LLC</td>
      <td>Multi-lateral bottom-line attitude</td>
      <td>756 Emma Loop\nNew Randallton, MA 34074</td>
      <td>001-403-947-8923x710</td>
      <td>lreed@example.net</td>
    </tr>
    <tr>
      <th>1</th>
      <td>inv_00002</td>
      <td>41242</td>
      <td>2001-08-07</td>
      <td>po_00002</td>
      <td>vendor_00002</td>
      <td>Mcconnell, Cook and Jacobs</td>
      <td>Multi-channeled 4thgeneration access</td>
      <td>3908 Moore Ferry Suite 731\nRileystad, OH 66846</td>
      <td>7967687131</td>
      <td>hscott@example.org</td>
    </tr>
    <tr>
      <th>2</th>
      <td>inv_00003</td>
      <td>93168</td>
      <td>2018-08-03</td>
      <td>po_00003</td>
      <td>vendor_00003</td>
      <td>Fowler PLC</td>
      <td>De-engineered analyzing matrix</td>
      <td>3744 Sarah Islands Apt. 917\nThompsonhaven, AK...</td>
      <td>881.131.6277x81348</td>
      <td>brandon73@example.com</td>
    </tr>
    <tr>
      <th>3</th>
      <td>inv_00004</td>
      <td>62921</td>
      <td>2003-07-08</td>
      <td>po_00004</td>
      <td>vendor_00004</td>
      <td>Washington, Jimenez and Melendez</td>
      <td>Horizontal 24/7 flexibility</td>
      <td>872 Ware Terrace\nLake Sarafort, NY 25369</td>
      <td>964.601.5818</td>
      <td>sramirez@example.org</td>
    </tr>
    <tr>
      <th>4</th>
      <td>inv_00005</td>
      <td>72479</td>
      <td>2000-10-01</td>
      <td>po_00005</td>
      <td>vendor_00005</td>
      <td>Johnson-Martinez</td>
      <td>Upgradable modular middleware</td>
      <td>2928 Dalton Station Apt. 170\nNorth Theresahav...</td>
      <td>(100)611-9164x12103</td>
      <td>danieljeanette@example.org</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>445</th>
      <td>inv_00446</td>
      <td>63753</td>
      <td>2014-08-19</td>
      <td>po_00059</td>
      <td>vendor_00059</td>
      <td>Romero, Miller and Cruz</td>
      <td>Configurable optimizing instruction set</td>
      <td>5751 Brian Green\nSouth Nicoleside, OR 95098</td>
      <td>751.189.4118x40072</td>
      <td>lbrewer@example.org</td>
    </tr>
    <tr>
      <th>446</th>
      <td>inv_00447</td>
      <td>114723</td>
      <td>2018-06-03</td>
      <td>po_00032</td>
      <td>vendor_00032</td>
      <td>Hill LLC</td>
      <td>Stand-alone regional intranet</td>
      <td>1052 Benjamin Spurs\nPort Carl, FL 75681</td>
      <td>(460)310-2789x04620</td>
      <td>michelle35@example.net</td>
    </tr>
    <tr>
      <th>447</th>
      <td>inv_00448</td>
      <td>45416</td>
      <td>2016-03-05</td>
      <td>po_00134</td>
      <td>vendor_00047</td>
      <td>Harris-Lyons</td>
      <td>Virtual value-added archive</td>
      <td>751 Paul Square\nNorth Raymondview, AL 26626</td>
      <td>+1-211-463-2487x4474</td>
      <td>terri31@example.net</td>
    </tr>
    <tr>
      <th>448</th>
      <td>inv_00449</td>
      <td>58418</td>
      <td>2018-09-27</td>
      <td>po_00052</td>
      <td>vendor_00052</td>
      <td>Thompson-Young</td>
      <td>Secured 3rdgeneration archive</td>
      <td>957 Sharon Lakes Suite 644\nSouth Victoriaside...</td>
      <td>0474775509</td>
      <td>edward24@example.net</td>
    </tr>
    <tr>
      <th>449</th>
      <td>inv_00450</td>
      <td>59770</td>
      <td>2018-08-31</td>
      <td>po_00101</td>
      <td>vendor_00041</td>
      <td>Wood, Mason and Lopez</td>
      <td>Visionary explicit software</td>
      <td>73688 Daugherty Coves\nPort Pamela, UT 76207</td>
      <td>574.997.1700</td>
      <td>stevenlowery@example.com</td>
    </tr>
  </tbody>
</table>
<p>450 rows × 10 columns</p>
</div>



## School

The school module allows you to generate fake school data


```python
import pandas as pd
from pydatafaker import school
skool =  school.create_school()
skool.keys()
skool['student_table']
skool['teacher_table']
skool['room_table']
skool['grade_table']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>student_id</th>
      <th>test_score</th>
      <th>date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>student_0009</td>
      <td>0.824952</td>
      <td>2020-12-27</td>
    </tr>
    <tr>
      <th>1</th>
      <td>student_0009</td>
      <td>0.651192</td>
      <td>2021-02-15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>student_0009</td>
      <td>0.884640</td>
      <td>2021-01-25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>student_0009</td>
      <td>0.862511</td>
      <td>2021-04-03</td>
    </tr>
    <tr>
      <th>4</th>
      <td>student_0009</td>
      <td>1.000000</td>
      <td>2021-01-18</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2995</th>
      <td>student_0300</td>
      <td>0.762023</td>
      <td>2021-06-02</td>
    </tr>
    <tr>
      <th>2996</th>
      <td>student_0300</td>
      <td>0.820461</td>
      <td>2020-12-10</td>
    </tr>
    <tr>
      <th>2997</th>
      <td>student_0300</td>
      <td>0.703434</td>
      <td>2021-07-25</td>
    </tr>
    <tr>
      <th>2998</th>
      <td>student_0300</td>
      <td>0.714107</td>
      <td>2021-04-14</td>
    </tr>
    <tr>
      <th>2999</th>
      <td>student_0300</td>
      <td>0.832456</td>
      <td>2020-10-30</td>
    </tr>
  </tbody>
</table>
<p>3000 rows × 3 columns</p>
</div>


