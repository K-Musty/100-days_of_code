from tkinter import *

# Window
window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="My Label", font=("Arial", 22, "bold"))
my_label.pack()

#Any of the below two can be used to change text
my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


my_button = Button(text="Click Me", command=button_clicked)
my_button.pack()

# Entry


input = Entry(width=10,)
input.pack()



window.mainloop()
