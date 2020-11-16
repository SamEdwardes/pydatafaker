![logo](https://raw.githubusercontent.com/SamEdwardes/pydatafaker/master/docs/source/_static/logo_with_grey_text.png)

![test_with_pytest](https://github.com/SamEdwardes/pydatafaker/workflows/test_with_pytest/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/pydatafaker/badge/?version=latest)](https://pydatafaker.readthedocs.io/en/latest/?badge=latest)

PyDataFaker is a python package to create fake data with relationships between tables. Creating fake data can be useful for many different applications such as creating product demos or testing software. 

Python already has a great package for creating fake data called Faker [https://faker.readthedocs.io/en/master/](https://faker.readthedocs.io/en/master/). Faker is great for creating individual fake units of data, but it can be time consuming to create more complicated fake data that is actually related to one another.

Imagine you are developing a new enterprise resource planning (ERP) software to challenge SAP. You may need to create some fake data to test your application. You will need an invoice table, a vendor listing, purchase order table, and more. PyDataFaker allows your to quickly create these tables and generates relationships between them!

PyDataFaker is currently under development. At this time it is possible to create the following entities:

- **Business**: create a fake business with common ERP like tables
- **School**: create a fake school

More entities are currently being developed. If you  have any ideas of additional entities that should be included please submit an issue here: [https://github.com/SamEdwardes/pydatafaker/issues](https://github.com/SamEdwardes/pydatafaker/issues).

## Table of contents

- [Installation](#installation)
- [Documentation](#documentation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Credits](#credits)

## Installation

```bash
pip install pydatafaker
```

## Documentation

Documentation can be found at [https://pydatafaker.readthedocs.io/en/latest/index.html](https://pydatafaker.readthedocs.io/en/latest/index.html). The package is distributed through PyPi at [https://pypi.org/project/pydatafaker/](https://pypi.org/project/pydatafaker/)

## Usage

### Business

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
biz['invoice_summary_table']
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>inv_00001</td>
      <td>59157</td>
      <td>2011-01-20</td>
      <td>po_00001</td>
      <td>vendor_00001</td>
    </tr>
    <tr>
      <th>1</th>
      <td>inv_00002</td>
      <td>87796</td>
      <td>2007-09-06</td>
      <td>po_00002</td>
      <td>vendor_00002</td>
    </tr>
    <tr>
      <th>2</th>
      <td>inv_00003</td>
      <td>57963</td>
      <td>2000-03-06</td>
      <td>po_00003</td>
      <td>vendor_00003</td>
    </tr>
    <tr>
      <th>3</th>
      <td>inv_00004</td>
      <td>59409</td>
      <td>2001-03-31</td>
      <td>po_00004</td>
      <td>vendor_00004</td>
    </tr>
    <tr>
      <th>4</th>
      <td>inv_00005</td>
      <td>86614</td>
      <td>2002-01-12</td>
      <td>po_00005</td>
      <td>vendor_00005</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>445</th>
      <td>inv_00446</td>
      <td>83316</td>
      <td>2012-09-02</td>
      <td>po_00087</td>
      <td>vendor_00087</td>
    </tr>
    <tr>
      <th>446</th>
      <td>inv_00447</td>
      <td>45707</td>
      <td>2008-07-10</td>
      <td>po_00101</td>
      <td>vendor_00098</td>
    </tr>
    <tr>
      <th>447</th>
      <td>inv_00448</td>
      <td>111932</td>
      <td>2002-09-26</td>
      <td>po_00158</td>
      <td>vendor_00012</td>
    </tr>
    <tr>
      <th>448</th>
      <td>inv_00449</td>
      <td>35104</td>
      <td>2012-09-21</td>
      <td>po_00133</td>
      <td>vendor_00075</td>
    </tr>
    <tr>
      <th>449</th>
      <td>inv_00450</td>
      <td>15397</td>
      <td>2015-12-15</td>
      <td>po_00054</td>
      <td>vendor_00054</td>
    </tr>
  </tbody>
</table>
<p>450 rows × 5 columns</p>
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
      <td>59157</td>
      <td>2011-01-20</td>
      <td>po_00001</td>
      <td>vendor_00001</td>
      <td>Smith-Scott</td>
      <td>Front-line multimedia emulation</td>
      <td>75343 Harper Corners Suite 581\nJuanberg, AK 0...</td>
      <td>(193)898-1652x129</td>
      <td>ftodd@example.org</td>
    </tr>
    <tr>
      <th>1</th>
      <td>inv_00002</td>
      <td>87796</td>
      <td>2007-09-06</td>
      <td>po_00002</td>
      <td>vendor_00002</td>
      <td>Walker-Morgan</td>
      <td>Cross-platform radical solution</td>
      <td>941 Susan Isle\nThorntonberg, KS 82841</td>
      <td>+1-636-744-9620x3991</td>
      <td>rdunn@example.com</td>
    </tr>
    <tr>
      <th>2</th>
      <td>inv_00003</td>
      <td>57963</td>
      <td>2000-03-06</td>
      <td>po_00003</td>
      <td>vendor_00003</td>
      <td>Noble and Sons</td>
      <td>Configurable demand-driven emulation</td>
      <td>1442 Jason Rapid Apt. 409\nEast Jade, RI 44983</td>
      <td>477-214-2021x973</td>
      <td>tinaschmidt@example.com</td>
    </tr>
    <tr>
      <th>3</th>
      <td>inv_00004</td>
      <td>59409</td>
      <td>2001-03-31</td>
      <td>po_00004</td>
      <td>vendor_00004</td>
      <td>Baker, Walker and Davenport</td>
      <td>Focused analyzing synergy</td>
      <td>89120 Kimberly Extensions\nSouth Annettetown, ...</td>
      <td>(643)621-7544x290</td>
      <td>sarahstephenson@example.com</td>
    </tr>
    <tr>
      <th>4</th>
      <td>inv_00005</td>
      <td>86614</td>
      <td>2002-01-12</td>
      <td>po_00005</td>
      <td>vendor_00005</td>
      <td>Patterson LLC</td>
      <td>Profound maximized productivity</td>
      <td>880 Bryan Tunnel Apt. 542\nKaylabury, AK 50221</td>
      <td>586-422-7311x0127</td>
      <td>littleyesenia@example.net</td>
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
      <td>83316</td>
      <td>2012-09-02</td>
      <td>po_00087</td>
      <td>vendor_00087</td>
      <td>Wagner-Gutierrez</td>
      <td>Multi-lateral motivating projection</td>
      <td>8771 Roger Road Suite 781\nDanielton, ID 88428</td>
      <td>001-023-820-3050x78454</td>
      <td>colliernicole@example.net</td>
    </tr>
    <tr>
      <th>446</th>
      <td>inv_00447</td>
      <td>45707</td>
      <td>2008-07-10</td>
      <td>po_00101</td>
      <td>vendor_00098</td>
      <td>Simmons-Leonard</td>
      <td>Focused reciprocal secured line</td>
      <td>9010 Ashley Mountains\nMarthaton, VT 68298</td>
      <td>391-162-6024</td>
      <td>serranonancy@example.org</td>
    </tr>
    <tr>
      <th>447</th>
      <td>inv_00448</td>
      <td>111932</td>
      <td>2002-09-26</td>
      <td>po_00158</td>
      <td>vendor_00012</td>
      <td>Welch LLC</td>
      <td>Versatile methodical interface</td>
      <td>4016 Brianna Road\nPort Andrealand, AR 22214</td>
      <td>+1-837-862-5571x172</td>
      <td>williamoliver@example.com</td>
    </tr>
    <tr>
      <th>448</th>
      <td>inv_00449</td>
      <td>35104</td>
      <td>2012-09-21</td>
      <td>po_00133</td>
      <td>vendor_00075</td>
      <td>Franklin-Bennett</td>
      <td>Digitized holistic methodology</td>
      <td>68125 Vega Plains Apt. 062\nEast Emily, OK 80097</td>
      <td>001-979-468-2358x530</td>
      <td>leroymoore@example.org</td>
    </tr>
    <tr>
      <th>449</th>
      <td>inv_00450</td>
      <td>15397</td>
      <td>2015-12-15</td>
      <td>po_00054</td>
      <td>vendor_00054</td>
      <td>Barton-Oneill</td>
      <td>Mandatory 4thgeneration hierarchy</td>
      <td>107 Julie Passage Suite 904\nSouth George, OH ...</td>
      <td>(491)397-7771x41615</td>
      <td>jacksonrachel@example.com</td>
    </tr>
  </tbody>
</table>
<p>450 rows × 10 columns</p>
</div>



### School


```python
import pandas as pd
from pydatafaker import school
skool =  school.create_school()
skool.keys()
skool['student_table']
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
      <th>name</th>
      <th>grade</th>
      <th>teacher_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>student_0001</td>
      <td>Tyler Campbell</td>
      <td>1</td>
      <td>teacher_0007</td>
    </tr>
    <tr>
      <th>1</th>
      <td>student_0003</td>
      <td>Melissa Coleman</td>
      <td>1</td>
      <td>teacher_0010</td>
    </tr>
    <tr>
      <th>2</th>
      <td>student_0011</td>
      <td>Crystal Church</td>
      <td>1</td>
      <td>teacher_0014</td>
    </tr>
    <tr>
      <th>3</th>
      <td>student_0017</td>
      <td>Paul Gray</td>
      <td>1</td>
      <td>teacher_0007</td>
    </tr>
    <tr>
      <th>4</th>
      <td>student_0023</td>
      <td>Joshua Morales</td>
      <td>1</td>
      <td>teacher_0010</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>31</th>
      <td>student_0258</td>
      <td>Nicole Hoffman</td>
      <td>7</td>
      <td>teacher_0015</td>
    </tr>
    <tr>
      <th>32</th>
      <td>student_0261</td>
      <td>Joseph Lewis</td>
      <td>7</td>
      <td>teacher_0009</td>
    </tr>
    <tr>
      <th>33</th>
      <td>student_0294</td>
      <td>Susan Jacobs</td>
      <td>7</td>
      <td>teacher_0015</td>
    </tr>
    <tr>
      <th>34</th>
      <td>student_0299</td>
      <td>Mark Whitehead</td>
      <td>7</td>
      <td>teacher_0009</td>
    </tr>
    <tr>
      <th>35</th>
      <td>student_0300</td>
      <td>Melissa Sosa</td>
      <td>7</td>
      <td>teacher_0015</td>
    </tr>
  </tbody>
</table>
<p>300 rows × 4 columns</p>
</div>



## Contributing

Please see [docs/source/contributing.rst](docs/source/contributing.rst).

## Credits

Developed by:

* Sam Edwardes

Logo:

* Icon made by [Freepik](https://www.flaticon.com/authors/freepik) from [www.flaticon.com](https://www.flaticon.com/)
* Front from [fontmeme.com/retro-fonts/](https://fontmeme.com/retro-fonts/)
* Logo generated using [logomakr.com](logomakr.com/7scB4)
