from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)

db = sqlite3.connect("books-collections.db")
cursor = db.cursor()
cursor.execute(" CREATE TABLE books(id INTEGER PRIMARY KEY, title VARCHAR(255) NOT NULL UNIQUE, author VARCHAR(255), rating FLOAT NOT NULL) ")

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

