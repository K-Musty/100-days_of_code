from tkinter import *

# Window
window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=25, pady=25)


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# Label
my_label = Label(text="My Label", font=("Arial", 22, "bold"))
my_label.grid(column=0, row=0)

# Any of the below two can be used to change text
my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button

my_button = Button(text="Click Me", command=button_clicked)
my_button.grid(column=1, row=1)
new_button = Button(text="New button", command=button_clicked)
new_button.grid(column=2, row=0)
# Entry

input = Entry(width=10)
input.grid(column=3, row=3)


window.mainloop()
