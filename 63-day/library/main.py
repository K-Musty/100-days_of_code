from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collections.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"

 # Required in newer Flask/SQLAlchemy versions
with app.app_context():
    db.create_all()

    # if not Book.query.get(1):
    #     # CREATE NEW BOOK
    #     new_book = Book(id=1, title="Harry Potter", author="J.K. Rowling", rating=9.3)
    #     db.session.add(new_book)
    #     db.session.commit()

    # READ ALL BOOKS
    # allbooks = db.session.query(Book).all()

    # READ SPECIFIC BOOK
    # specific_book = Book.query.filter_by(title="Harry Potter").first()

    # UPDATE A RECORD BY QUERY
    # book_to_update = Book.query.filter_by(title="Harry Potter").first()
    # book_to_update.title = "Harry Potter and the Chamber of Secrets"
    # db.session.commit()


#
# db = sqlite3.connect("books-collections.db")
# cursor = db.cursor()
# cursor.execute(" CREATE TABLE books(id INTEGER PRIMARY KEY, title VARCHAR(255) NOT NULL UNIQUE, author VARCHAR(255), rating FLOAT NOT NULL) ")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


# all_books = []

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == 'POST':

        new_book = Book(
        title= request.form['title'],
        author= request.form['author'],
        rating= request.form['rating']
        )
        with app.app_context():
            db.session.add(new_book)
            db.session.commit()

        return redirect(url_for('home'))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

