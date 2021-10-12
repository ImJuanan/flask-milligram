Flask-Milligram
===============

`Milligram <https://milligram.io/>`_ — a minimalist CSS framework — helper for Jinja2 template engine in Flask.


Contents
--------

.. toctree::
   :maxdepth: 2
   
   basic
   macros
   examples


Changelog
---------

.. toctree::
   :maxdepth: 2

   changelog


Development
-----------

All kinds of contributions are meaningful.
You can build the development environment locally and run tests using tox with the following commands:

.. code-block:: bash

    $ git clone https://github.com/ImJuanan/flask-milligram.git
    $ cd flask-milligram
    $ pipenv install
    $ pipenv run pip install ".[dev]"
    $ pipenv run tox

If you are not familiar with Pipenv, this way is gonna work as well:

.. code-block:: bash

    $ git clone https://github.com/ImJuanan/flask-milligram.git
    $ cd flask-milligram
    $ python -m venv env
    $ env/Scripts/activate
    $ pip install ".[dev]"
    $ tox


Authors
-------

Maintainer: `Juan An <https://www.yangxk196.com>`_


License
-------

This project is licensed under the MIT License (see the
``LICENSE`` file for details).
