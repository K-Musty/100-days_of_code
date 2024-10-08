from tkinter import *
from tkinter import messagebox
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
data = {}
random_word = {}
try:
    panda_data = pandas.read_csv("data/words_to_learn.csv")
    # stuff = pandas.DataFrame(french_data)
    # french_list = stuff["French"]
except pandas.errors.EmptyDataError:
    original_panda_data = pandas.read_csv("data/french_words.csv",)
    data = original_panda_data.to_dict(orient="records")
else:
    data = panda_data.to_dict(orient="records")


def next_cards():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(data)
    if len(random_word) == 0:
        messagebox.showinfo(title="Alert", message="You've exhausted all words")
    canvas.itemconfig(word, text=random_word["French"], fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    flip_timer = window.after(3000, show_english)
    canvas.itemconfig(image_front, image=card_front,)


def show_english():
    canvas.itemconfig(image_front, image=card_back)
    canvas.itemconfig(word, text=random_word["English"], fill="white")
    canvas.itemconfig(title, text="English", fill="white")


def known_cards():
    data.remove(random_word)
    learning_data = pandas.DataFrame(data)
    learning_data.to_csv("data/words_to_learn.csv", index=False)
    next_cards()
# ---------------------------- UI -------------------------------------- #


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, show_english)

# Canvas
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
image_front = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="", font=("Arial", 20, "italic"), fill="black")
word = canvas.create_text(400, 263, text="", font=("Arial", 20, "italic"), fill="black")
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
# Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=known_cards)
right_button.grid(column=1, row=1)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_cards)
wrong_button.grid(column=0, row=1)


next_cards()

window.mainloop()
