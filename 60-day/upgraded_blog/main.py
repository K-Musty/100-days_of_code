from flask import Flask, render_template, request
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


@app.route("/index")
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:num>")
def show_post(num):
    requested_blog = None
    for post in posts:
        if post.post_id == num:
            requested_blog = post
    return render_template("post.html", blog_post=requested_blog)


@app.route("/contact", methods=["POST" , "GET"])
def contact():
    status = False
    message = None
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        message =  "Successfully sent your message"
        status = True

    return render_template("contact.html", message=message, status=status)

if __name__ == "__main__":
    app.run(debug=True)