from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

API_KEY = ""
MOVIE_URL = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
MOVIE_DETAIL_URL = "https://api.themoviedb.org/3/movie"


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


class MyForm(FlaskForm):
    new_rating = StringField("Your Rating out of 10 e.g 7.5", [DataRequired()])
    new_review = StringField("Your Review", [DataRequired()])
    submit = SubmitField("Done")

class AddForm(FlaskForm):
    movie_title = StringField("Movie Title")
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    all_movies = db.session.query(Movies).all()
    print(all_movies)
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=['POST', 'GET'])
def edit_rating():
    form = MyForm()
    movie_id = request.args.get("id")
    movie = Movies.query.get(movie_id)
    if movie is None:
        # Handle the case where the movie isn't found
        return redirect(url_for('home'))
    if form.validate_on_submit():
        movie.rating = float(form.new_rating.data)
        movie.review = form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form)

@app.route("/delete", methods=['POST', 'GET'])
def delete():
    movie_id = request.args.get("id")
    movie = Movies.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=['POST', 'GET'])
def add_movie():
    form = AddForm()
    if form.validate_on_submit():
        movie_title = form.movie_title.data
        response = requests.get(MOVIE_URL, params={"api_key": API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)

    return render_template("add.html", form=form)

@app.route("/movie")
def select_movie():
    movie_api_id = request.args.get("id")
    print(movie_api_id)
    if movie_api_id:
        movie_url = f"{MOVIE_DETAIL_URL}/{movie_api_id}"
        response = requests.get(url=movie_url, params={"api_key": API_KEY, "language": "en-US"})
        data = response.json()
        print(data)
        new_movie = Movies(
            title = data["title"],
            year = data["release_date"].split("-")[0],
            img_url = f'{MOVIE_DETAIL_URL}/{data["poster_path"]}',
            description = data['overview']
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("select.html")


if __name__ == '__main__':
    app.run(debug=True)
