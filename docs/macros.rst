Macros
======

render_navbar()
----------------
Render a navigation header

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'milligram/nav.html' import render_navbar %}

    {{ render_navbar([('index', 'Home'), ('other', 'Other'), ('about', 'About')])}}

API
~~~~

.. py:function:: render_navbar(navigation)

    :param navigation: An iterable object contains several tuples or lists where the first element is the endpoint used to generate URL and second is the text displayed.


render_breadcrumb()
--------------------
Render a navigation breadcrumb.

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'milligram/nav.html' import render_breadcrumb %}

    {{ render_breadcrumb([('index', 'Home'), ('other', 'Other'), ('about', 'About')], use_ol=True)}}

API
~~~~

.. py:function:: render_breadcrumb(navigation, use_ol=False)

    :param navigation: An iterable object contains several tuples or lists where the first element is the endpoint used to generate URL and second is the text displayed.
    :param use_ol: Default to generate ``<ul></ul>``, if set to ``True``, it will generate ``<ol></ol>``.


render_pagination()
--------------------
Render a Flask-SQLAlchemy pagniantion.

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'milligram/pagination.html' import render_pagination %}

    {{ render_pagination(pagination) }}

API
~~~~

.. py:function:: render_pagination(pagination, fragment='', endpoint=None, ellipses='…')

    :param pagination: :class:`~flask_sqlalchemy.Pagination` instance.
    :param fragment: Add URL fragment into link.
    :param endpoint: Which endpoint to call when a page number is clicked.
    :param ellipses: Symbol to use to indicate that pages have been skipped.


render_badge()
---------------
Render a badge.

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'milligram/utilities.html' import render_badge %}

    {{ render_badge('Badge') }}

API
~~~~

.. py:function:: render_badge(text, small=False)

    :param text: Text displayed in the badge.
    :param small: Default to generate a normal size badge, if set to ``True``, it will generate a small size badge.
