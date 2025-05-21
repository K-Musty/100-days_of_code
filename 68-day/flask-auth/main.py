from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

# Line below only required once, when creating DB.
# with app.app_context():
#     db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')


        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please login or use a different email.')
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            password=request.form.get('password'),
            salt_length=8,
            method='pbkdf2:sha256'
        )
        new_user = User(
            email=email,
            name=request.form.get('name'),
            password=hash_and_salted_password
        )
        db.session.add(new_user)
        db.session.commit()

        # Log in the new user
        login_user(new_user)

        return redirect(url_for('secrets'))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif  not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('secrets'))

    return render_template("login.html", logged_in=current_user.is_authenticated)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/secrets')
@login_required
def secrets():
    user_name = current_user.name
    return render_template("secrets.html", name=user_name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return "You are now Logged out"


@app.route('/download')
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf", )


if __name__ == "__main__":
    app.run(debug=True)
