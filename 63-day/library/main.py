from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new_books-collections.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    author = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


db.create_all()

#
# db = sqlite3.connect("books-collections.db")
# cursor = db.cursor()
# cursor.execute(" CREATE TABLE books(id INTEGER PRIMARY KEY, title VARCHAR(255) NOT NULL UNIQUE, author VARCHAR(255), rating FLOAT NOT NULL) ")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


all_books = []

@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == 'POST':

        books_dict = {
        'title': request.form['title'],
        'author': request.form['author'],
        'rating': request.form['rating']
        }
        all_books.append(books_dict)

        return redirect(url_for('home'))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

