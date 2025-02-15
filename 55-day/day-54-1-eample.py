import time
from flask import Flask

app = Flask(__name__)

@app.route("/")
def greet():
    return "Hello"

@app.route("/<abba>/<int:num>")
def display(abba, num):
    return f"Hello {abba} for {num} everything"

if __name__ == "__main__":
    app.run(debug=True)