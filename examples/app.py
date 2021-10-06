# -*- coding: utf-8 -*-
import random

from flask import Flask, render_template, request

from flask_milligram import Milligram
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

milligram = Milligram(app)
db = SQLAlchemy(app)


class Movie(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(55), nullable=False)
    genre = db.Column(db.String(55), nullable=False)
    publish_year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)


@app.before_first_request
def generate_fake_data():
    db.drop_all()
    db.create_all()
    for i in range(30):
        m = Movie(
            title=f'Title {i + 1}',
            genre=f'Genre {i + 1}',
            publish_year=random.randint(2000, 2021),
            rating=round(random.uniform(0, 5), 1)
        )
        db.session.add(m)
    db.session.commit()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/nav')
def test_nav():
    return render_template('nav.html')


@app.route('/pagination')
def test_pagination():
    page = request.args.get('page', 1, type=int)
    pagination = Movie.query.paginate(page, per_page=6)
    movies = pagination.items
    return render_template('pagination.html', pagination=pagination, movies=movies)


@app.route('/badge')
def test_badge():
    return render_template('badge.html')


if __name__ == '__main__':
    app.run(debug=True)
