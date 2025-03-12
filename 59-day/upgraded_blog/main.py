from flask import Flask, render_template
import requests

URL = "https://api.npoint.io/bd5493b8744a52d09b8b"

response = requests.get(url=URL)
all_posts = response.json()
app = Flask(__name__)

@app.route("/index.html")
def home():
    # for posts in all_posts:
    #     post_id = posts["id"]
    #     title = posts["title"]
    #     subtitle = posts["subtitle"]
    #     body = posts["body"]

    return render_template("index.html", posts=all_posts)

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/post.html")
def post():
    return render_template("post.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)