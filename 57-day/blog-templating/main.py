from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/25bdf096de4e3edde919"
response = requests.get(blog_url)
blog_posts = response.json()
posts = []
for i in blog_posts:
    post = Post(i["id"], i["title"], i["subtitle"], i["body"])
    posts.append(post)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route("/blog/<int:num>")
def blog_post(num):
    requested_post = None
    for blog_post in posts:
        if blog_post.post_id == num:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
