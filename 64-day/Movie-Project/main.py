from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top_ten_movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(250), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(300), nullable=False)
    img_url = db.Column(db.String(300), nullable=False)


with app.app_context():
    db.create_all()

    # new_movie = Movies(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )
    #
    # db.session.add(new_movie)
    # db.session.commit()

@app.route("/")
def home():
    all_movies = db.session.query(Movies).all()
    print(all_movies)
    return render_template("index.html", movies=all_movies)


if __name__ == '__main__':
    app.run(debug=True)
