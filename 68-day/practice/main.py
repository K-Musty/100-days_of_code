from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_required, logout_user, current_user, login_user

app = Flask(__name__)

app.config['SECRET_KEY'] = "ascretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///login.db"

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)


with app.app_context():
    db.create_all()  # This creates all database tables

    # Check if user already exists before adding
    # if not User.query.filter_by(name="Kalli").first():
    #     abba_kalli = User(name="Kalli")  # Proper initialization
    #     db.session.add(abba_kalli)
    #     db.session.commit()
    #     print("User 'Kalli' added to database")
    # else:
    #     print("User 'Kalli' already exists")

@login_manager.user_loader
def load_user(user_id):
    if user_id is None:
        return None
    try:
        return User.query.get(int(user_id))
    except (ValueError, TypeError):
        return None


@app.route("/")
def index():
    user = User.query.filter_by(name='Kalli').first()
    login_user(user)
    return f"Hello {user.name if user else 'Guest'} you are now logged in"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "You are now Logged out"

@app.route("/home")
@login_required
def home():
    return "Current user is " + current_user.name

if __name__ == ('__main__'):
    app.run(debug=True)