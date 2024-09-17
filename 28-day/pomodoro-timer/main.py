from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():

    count_down(5 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(text_count, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=200, pady=50, background=YELLOW)
window.minsize(width=750, height=500)

# Canvas
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png",)
canvas.create_image(100, 112, image=tomato_img)
text_count = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)

# Labels
timer_label = Label(text="Timer", foreground=GREEN, highlightthickness=0, background=YELLOW,
                    font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)
tick_label = Label(text="✔", foreground=GREEN, highlightthickness=0, background=YELLOW, font=(FONT_NAME, 30, "bold"))
tick_label.grid(column=1, row=3)

# Buttons
start_button = Button(text="Start", background="white", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", background="white", highlightthickness=0)
reset_button.grid(column=2, row=2)


window.mainloop()
