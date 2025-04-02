from flask import Flask
from flask.globals import app_ctx
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///practice_users.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()

    # Create new user
    if not User.query.get(1):

        new_user = User(id=1, name="Abba", email="abba@abba", password="1234")
        db.session.add(new_user)
        db.session.commit()

    # To read all users
    all_users = db.session.query(User).all()
    for user in all_users:
        id = user.id
        name = user.name
        email = user.email
        password = user.password

    print(f"{id}, Name= {name}, Email= {email}, Password= {password}")

    # Single User from table

    user = User.query.first()
    print("""
    ┌───────────────────────────
    │ USER #{}
    ├───────────────────────────
    │ Name:    {}
    │ Email:   {}
    └───────────────────────────
    """.format(
        user.id,
        user.name,
        user.email
    ))

if __name__ == "__main__":
    app.run()