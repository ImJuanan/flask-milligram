# -*- coding: utf-8 -*-
"""
    flask_milligram
    ~~~~~~~~~~~~~~
    Milligram — a minimalist CSS framework — helper for Jinja2 template engine in Flask.

    :author: Juan An <yangxk196@163.com>
    :copyright: (c) 2021 by Juan An.
    :license: MIT, see LICENSE for more details.
"""
from flask import current_app, Markup, Blueprint, url_for


class Milligram:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['milligram'] = self

        blueprint = Blueprint('milligram', __name__, static_folder='static',
                              static_url_path=f'/milligram{app.static_url_path}',
                              template_folder='templates')
        app.register_blueprint(blueprint)

        app.jinja_env.globals['milligram'] = self
        app.jinja_env.add_extension('jinja2.ext.do')

        app.config.setdefault('MILLIGRAM_SERVE_LOCAL', False)

    @staticmethod
    def load_css(css_normalize_url=None, css_url=None):
        """Load Milligram and extended css resources.

        :param css_normalize_url: if set, will be used as css url of Normalize.
        :param css_url: if set, will be used as css url of Milligram.
        """
        serve_local = current_app.config['MILLIGRAM_SERVE_LOCAL']

        if serve_local:
            css_normalize_url = url_for(
                'milligram.static', filename='css/normalize.min.css')
            css_url = url_for('milligram.static',
                              filename='css/milligram.min.css')
        else:
            if css_normalize_url is None:
                css_normalize_url = 'https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css'
            if css_url is None:
                css_url = 'https://cdnjs.cloudflare.com/ajax/libs/milligram/1.4.1/milligram.min.css'

        css_extensions_url = url_for(
            'milligram.static', filename='css/milligram-extensions.min.css')
        return Markup(f'''<link rel="stylesheet" href="{css_normalize_url}" />\n
            <link rel="stylesheet" href="{css_url}" />\n
            <link rel="stylesheet" href="{css_extensions_url}" />''')

    @staticmethod
    def load_js():
        """Load related js resource locally.
        """
        js_url = url_for('milligram.static',
                         filename='js/milligram-extensions.js')
        return Markup(f'<script src="{js_url}"></script>')
