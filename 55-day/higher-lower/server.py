import random
from flask import Flask

number_to_guess = random.randint(1,9)
colors = ['yellow', 'blue', 'orange', 'green', 'teal', 'purple']

app = Flask(__name__)

@app.route("/")
def index():
    return (f"<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")


@app.route("/<int:number>")
def higher_lower(number):
    color = random.choice(colors)
    if number < number_to_guess:
        return (f"<h1 style='color: {color};'>{number} is too Low</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")
    elif number > number_to_guess:
        return (f"<h1 style='color: {color};'>{number}; is too high</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")
    elif number == number_to_guess:
        return (f"<h1 style='color: {color};'>{number} is just right</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")


if __name__ == "__main__":
    app.run()