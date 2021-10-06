"""
    flask_milligram
    ~~~~~~~~~~~~~~
    Milligram — a minimalist CSS framework — helper for Jinja2 template engine in Flask.

    :author: Juan An <yangxk196@163.com>
    :copyright: (c) 2021 by Juan An.
    :license: MIT, see LICENSE for more details.
"""
import unittest

from flask import Flask, render_template_string, request, current_app
from flask_sqlalchemy import SQLAlchemy

from flask_milligram import Milligram


class MilligramTestCase(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.milligram = Milligram(app)

        @app.route('/')
        def index():
            return render_template_string('{{ milligram.load_css() }}{{ milligram.load_js() }}')

        self.context = app.test_request_context()
        self.context.push()
        self.client = app.test_client()

    def tearDown(self):
        self.context.pop()

    def test_extension_init(self):
        self.assertIn('milligram', current_app.extensions)

    def test_config(self):
        self.assertIn('MILLIGRAM_SERVE_LOCAL', current_app.config)
        self.assertEqual(current_app.config['MILLIGRAM_SERVE_LOCAL'], False)

    def test_load_css(self):
        rv = self.milligram.load_css()
        self.assertIn(
            'https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css', rv)
        self.assertIn(
            'https://cdnjs.cloudflare.com/ajax/libs/milligram/1.4.1/milligram.min.css', rv)
        self.assertIn(
            'milligram-extensions.min.css', rv)

    def test_load_js(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertIn('milligram-extensions.js', data)

    def test_local_resources(self):
        current_app.config['MILLIGRAM_SERVE_LOCAL'] = True

        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertIn('normalize.min.css', data)
        self.assertIn('milligram.min.css', data)
        self.assertIn('milligram-extensions.min.css', data)

    def test_render_navbar(self):
        @current_app.route('/navbar')
        def nav():
            return render_template_string('''
                {% from 'milligram/nav.html' import render_navbar %}
                {{ render_navbar([('nav', 'Nav')]) }}
                ''')

        response = self.client.get('/navbar')
        data = response.get_data(as_text=True)
        self.assertIn('<ul class="nav__list collapsible__content">', data)
        self.assertIn('<li class="nav__item">', data)
        self.assertIn('<a class="active"', data)

        @current_app.route('/nav_not_active')
        def nav_not_active():
            return render_template_string('''
                {% from 'milligram/nav.html' import render_navbar %}
                {{ render_navbar([('nav', 'Nav')]) }}
                ''')

        response = self.client.get('/nav_not_active')
        data = response.get_data(as_text=True)
        self.assertNotIn('<a class="active"', data)

    def test_render_breadcrumb(self):
        @current_app.route('/breadcrumb')
        def bc():
            return render_template_string('''
                {% from 'milligram/nav.html' import render_breadcrumb %}
                {{ render_breadcrumb([('bc', 'Breadcrumb')], use_ol=True) }}
                ''')

        response = self.client.get('/breadcrumb')
        data = response.get_data(as_text=True)
        self.assertIn('<ol class="breadcrumb">', data)
        self.assertIn('<li class="breadcrumb-item">', data)
        self.assertIn('<a class="active"', data)

        @current_app.route('/bc_not_active')
        def bc_not_active():
            return render_template_string('''
                {% from 'milligram/nav.html' import render_breadcrumb %}
                {{ render_breadcrumb([('bc', 'Breadcrumb')]) }}
                ''')

        response = self.client.get('/bc_not_active')
        data = response.get_data(as_text=True)
        self.assertIn('<ul class="breadcrumb">', data)
        self.assertNotIn('<a class="active"', data)

    def test_render_pagination(self):
        db = SQLAlchemy(current_app)

        class Movie(db.Model):
            _id = db.Column(db.Integer, primary_key=True)

        @current_app.route('/pagination')
        def pagination():
            db.drop_all()
            db.create_all()
            for i in range(100):
                m = Movie()
                db.session.add(m)
            db.session.commit()
            page = request.args.get('page', 1, type=int)
            pagination = Movie.query.paginate(page, per_page=10)
            movies = pagination.items
            return render_template_string('''
                                    {% from 'milligram/pagination.html' import render_pagination %}
                                    {{ render_pagination(pagination) }}
                                    ''', pagination=pagination, movies=movies)

        response = self.client.get('/pagination')
        data = response.get_data(as_text=True)
        self.assertIn('<nav>', data)
        self.assertIn('<ul class="pagination">', data)
        self.assertIn('<li class="page-item">', data)
        self.assertIn('<a class="page-link" href="#">1</a>', data)
        self.assertIn('10</a>', data)

        response = self.client.get('/pagination?page=2')
        data = response.get_data(as_text=True)
        self.assertIn('<li class="page-item active">', data)
        self.assertIn('1</a>', data)
        self.assertIn('<a class="page-link" href="#">2</a>', data)

    def test_render_badge(self):
        @current_app.route('/badge')
        def badge():
            return render_template_string('''
                {% from 'milligram/utilities.html' import render_badge %}
                {{ render_badge('Badge') }}
                {{ render_badge('Badge', small=True) }}
                ''')

        response = self.client.get('/badge')
        data = response.get_data(as_text=True)
        self.assertIn('<span class="badge">Badge</span>', data)
        self.assertIn('<span class="badge badge--small">Badge</span>', data)


if __name__ == '__main__':
    unittest.main()
