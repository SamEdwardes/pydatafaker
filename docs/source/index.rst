.. PyDataFaker documentation master file, created by
   sphinx-quickstart on Wed Sep  2 21:04:29 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyDataFaker's documentation!
=======================================

PyDataFaker is a python package to generate fake data. *Data base* style data can be generated, meaning tables with relationships between them are created.


===========
Quick Start
===========

PyDataFaker can be installed from `PyPi <https://pypi.org/project/pydatafaker/>`_ by running:

.. code-block:: bash
    :linenos:

    pip install pydatafaker

Easily create fake business data:

.. code-block:: python
    :linenos:

    from pydata faker import business

    biz = business.create_business()

=================
Table of Contents
=================

.. toctree::
   :maxdepth: 2

   usage
   api_reference
   contributing

=======
Credits
=======

The source code for PyDataFaker is hosted on github at `https://github.com/SamEdwardes/pydatafaker <https://github.com/SamEdwardes/pydatafaker>`_.

Developed by:

* Sam Edwardes

Logo:

* Icon made by `Freepik <https://www.flaticon.com/authors/freepik>`_ from `www.flaticon.com <https://www.flaticon.com/>`_
* Front from `fontmeme.com/retro-fonts/ <https://fontmeme.com/retro-fonts/>`_
* Logo generated using `logomakr.com <logomakr.com/7scB4l>`_
