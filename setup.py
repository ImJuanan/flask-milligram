# -*- coding: utf-8 -*-
"""
Flask-Milligram
---------------

[Milligram](https://milligram.io/) — a minimalist CSS framework — helper for Jinja2 template engine in Flask.

Check out the [documentation](https://flask-milligram.readthedocs.io/) or
[GitHub repo](https://github.com/ImJuanan/flask-milligram) for more details.
"""
from setuptools import setup

setup(
    name='Flask-Milligram',
    version='0.1.0',
    url='https://github.com/ImJuanan/flask-milligram',
    license='MIT',
    author='Juan An',
    author_email='yangxk196@163.com',
    description='Milligram — a minimalist CSS framework — helper for Jinja2 template engine in Flask.',
    long_description=__doc__,
    long_description_content_type='text/markdown',
    platforms='any',
    packages=['flask_milligram'],
    zip_safe=False,
    include_package_data=True,
    test_suite='test_flask_milligram',
    install_requires=[
        'Flask'
    ],
    tests_require=[
        'flask_sqlalchemy'
    ],
    extras_require={
        'dev': [
            'coverage',
            'flake8',
            'tox'
        ]
    },
    keywords='flask extension development',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
