from flask import Flask, render_template
import requests
from post import Post

URL = "https://api.npoint.io/bd5493b8744a52d09b8b"

response = requests.get(url=URL)
all_posts = response.json()
app = Flask(__name__)
posts = []
for i in all_posts:
    post = Post(i["id"], i["title"], i["subtitle"], i["body"],)
    posts.append(post)


@app.route("/index.html")
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/post.html/<int:num>")
def show_post(num):
    requested_blog = None
    for post in posts:
        if post.post_id == num:
            requested_blog = post
    return render_template("post.html", blog_post=requested_blog)


@app.route("/contact.html")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)