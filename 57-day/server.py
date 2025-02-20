import datetime
from flask import Flask, render_template


app =  Flask(__name__)

@app.route("/")
def home():
    year = datetime.date.today().year
    return render_template("index.html", today=year)

if __name__ == "__main__":
    app.run(debug=True)