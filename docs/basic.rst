Basic
=====

Installation
------------

.. code-block:: bash

    $ pip install flask-milligram


Initialization
--------------

.. code-block:: python

    from flask_milligram import Milligram
    from flask import Flask

    app = Flask(__name__)

    milligram = Milligram(app)


Load Resources
-----------------

Flask-Milligram provides two methods to load related resources in the template:
``milligram.load_css`` and ``milligram.load_js``.

You need to call them in your base template first:

.. code-block:: jinja

    <head>
    ....
    {{ milligram.load_css() }}
    </head>
    <body>
    ...
    {{ milligram.load_js() }}
    </body>

By default, normalize.css and milligram.css loaded from CDN. Set ``MILLIGRAM_SERVE_LOCAL`` to ``True`` to use built-in local files.
Please note that these two methods are not optional, that is to say, Flask-Milligram cannot run without the related resources espectially milligram-extensions.css and milligram-extensions.js.
However, you can customize them anytime you want.


Base template
----------------

Here is an example base template you can use:

.. code-block:: html

    <!doctype html>
    <html lang="en">
        <head>
            {% block head %}
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

            {% block styles %}
                {{ milligram.load_css() }}
            {% endblock %}

            <title>Page title</title>
            {% endblock %}
        </head>
        <body>
            {% block content %}{% endblock %}

            {% block scripts %}
                {{ milligram.load_js() }}
            {% endblock %}
        </body>
    </html>

.. _macros_list:


Macros
------

+---------------------------+--------------------------------+----------------------------------------+
| Macro                     | Templates Path                 | Description                            |
+===========================+================================+========================================+
| render_navbar()           | milligram/nav.html             | Render a navigation header             |
+---------------------------+--------------------------------+----------------------------------------+
| render_breadcrumb()       | milligram/nav.html             | Render a navigation breadcrumb         |
+---------------------------+--------------------------------+----------------------------------------+
| render_pagination()       | milligram/pagination.html      | Render a Flask-SQLAlchemy pagniantion  |
+---------------------------+--------------------------------+----------------------------------------+
| render_badge()            | milligram/utilities.html       | Render a badge                         |
+---------------------------+--------------------------------+----------------------------------------+

Import the macros above from the corresponding path and call them in template engine:

.. code-block:: jinja

    {% from 'milligram/pagination.html' import render_pagination %}

    {{ render_pagination(pagination) }}

Go to the :doc:`macros` page to see more details.


Configurations
--------------

+-----------------------------+----------------------+-------------------------------------------------------------------------------+
| Configuration Variable      | Default Value        | Description                                                                   |
+=============================+======================+===============================================================================+
| MILLIGRAM_SERVE_LOCAL       | ``False``            | If set to ``True``, local resources will be used for ``load_css`` methods.    |
+-----------------------------+----------------------+-------------------------------------------------------------------------------+

