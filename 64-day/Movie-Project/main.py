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

class MyForm(FlaskForm):
    new_rating = StringField("Your Rating out of 10 e.g 7.5", [DataRequired()])
    new_review = StringField("Your Review", [DataRequired()])
    submit = SubmitField("Done")


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

if __name__ == '__main__':
    app.run(debug=True)
