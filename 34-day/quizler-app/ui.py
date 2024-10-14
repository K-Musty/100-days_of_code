from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=100, pady=100, background=THEME_COLOR)
        # Score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas for displaying questions
        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Question goes here ", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        self.right_image = PhotoImage(file="images/true.png")
        self.right_answer = Button(width=100, height=100, image=self.right_image, highlightthickness=0, command=self.true_clicked)
        self.right_answer.grid(row=2, column=0)
        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_answer = Button(width=100, height=100, image=self.wrong_image, highlightthickness=0, command=self.false_clicked)
        self.wrong_answer.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz" )
            self.right_answer.config(state="disabled")
            self.wrong_answer.config(state="disabled")

    def true_clicked(self):
        self.get_feedback(self.quiz.check_answer("True"))
    def false_clicked(self):
        is_right = self.quiz.check_answer("False")
        self.get_feedback(is_right)

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)