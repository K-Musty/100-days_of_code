import datetime
import requests
from flask import Flask, render_template


app =  Flask(__name__)

@app.route("/")
def home():
    year = datetime.date.today().year
    return render_template("index.html", today=year)

@app.route("/guess/<name>")
def guess(name):
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age_data = age_response.json()
    age = age_data["age"]
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    return render_template("guess.html", age=age, gender=gender, name=name)

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/25bdf096de4e3edde919"
    response = requests.get(blog_url)
    blog_posts = response.json()
    return render_template("blog.html", posts=blog_posts)

if __name__ == "__main__":
    app.run(debug=True)