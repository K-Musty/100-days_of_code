from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.secret_key = ""

class MyForm(FlaskForm):
    name = StringField('name', [DataRequired()])
    email = EmailField('email', [DataRequired()])
    password = PasswordField('password', [DataRequired()])



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    form = MyForm()
    # if form.validate_on_submit():
    #     return redirect("/Success")
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)