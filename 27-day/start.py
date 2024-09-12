import tkinter

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=500)

# Label
my_label = tkinter.Label(text="My Label", font=("Arial", 22, "italic"))
my_label.pack()


window.mainloop()
