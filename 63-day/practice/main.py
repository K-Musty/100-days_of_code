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


if __name__ == "__main__":
    app.run()