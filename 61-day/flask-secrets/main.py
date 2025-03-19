from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)

app.secret_key = "11111111111111111111"

class MyForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    email = EmailField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired(), Length(min=8)])
    submit = SubmitField("Log in")



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST', 'DELETE'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)