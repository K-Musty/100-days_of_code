from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=100, pady=100, background=THEME_COLOR)

        self.score_label = Label()
        self.score_label.config(text="Score")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=200, height=200, background="white", highlightthickness=0)
        self.canvas.create_window(width=200, height=200)
        self.canvas.grid(column=1, row=1, coloumnspan=2)
        self.right_answer = Button(padx=25, pady=25)
        self.right_answer.grid(row=1, column=0,)
        self.wrong_answer = Button(padx=25, pady=25)
        self.wrong_answer.grid(row=1, column=1)


        self.window.mainloop()