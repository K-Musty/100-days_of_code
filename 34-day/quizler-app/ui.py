from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=100, pady=100, background=THEME_COLOR)
        # Score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas for displaying questions
        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Question goes here ", width=280, fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        right_image = PhotoImage(file="images/true.png", width=100, height=100)
        self.right_answer = Button(padx=25, pady=25, background=right_image)
        self.right_answer.grid(row=2, column=0)
        wrong_image = PhotoImage(file="images/false.png", width=100, height=100)
        self.wrong_answer = Button(padx=25, pady=25, background=wrong_image)
        self.wrong_answer.grid(row=2, column=1)

        self.window.mainloop()
