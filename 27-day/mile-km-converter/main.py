from tkinter import *


# Function to take action
def calculate_km():
    mile = float(input_mile.get())
    km = round(mile * 1.609)
    label_ans.config(text=km)


# Window
window = Tk()
window.title("MIle to km converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

# Label
label = Label(text="Mile",)
label.grid(column=3, row=1)
label_equal = Label(text="is equal to")
label_equal.grid(column=1, row=2)
label_km = Label(text="Km")
label_km.grid(column=3, row=2)
label_ans = Label()
label_ans.grid(column=2, row=2)

# Entry
input_mile = Entry(width=15, highlightcolor="blue")
input_mile.grid(column=2, row=1)

# Button to calculate
button = Button(text="Calculate", command=calculate_km, width=20)
button.grid(column=2, row=3)

window.mainloop()
