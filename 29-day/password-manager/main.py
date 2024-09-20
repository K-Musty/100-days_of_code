from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
               'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for sym in range(randint(2, 4))]
    password_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()

    if len(email) == 0 or len(password) == 0 or len(website) == 0:
        messagebox.showerror(title="Error", message="Parameter missing")
    else:

        # messagebox.showinfo(title="Title", message="Message")
        is_ok = messagebox.askokcancel(title=website, message=f"This are the details you've entered\nEmail:{email}\n"
                                                              f" Password: {password}\n Is it OK to save? ")
        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
# window.minsize(width=750, height=500)
window.config(padx=100, pady=100, background="white")

canvas = Canvas(width=200, height=200, background="white", highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ", background="white")
website_label.grid(column=0, row=2)

user_label = Label(text="Email/Username: ", background="white")
user_label.grid(column=0, row=3)

password_label = Label(text="Password: ", background="white")
password_label.grid(column=0, row=4)

# Entries
website_entry = Entry(width=41)
website_entry.grid(column=1, row=2, columnspan=2)
website_entry.focus()

user_entry = Entry(width=41)
user_entry.grid(column=1, row=3, columnspan=2)
user_entry.insert(0, "kmustapha9564@gmail.com")

password_entry = Entry(width=23)
password_entry.grid(column=1, row=4)

# Buttons
gen_password_button = Button(text="Generate Password", width=14, command=generate_password)
gen_password_button.grid(column=2, row=4)

add_button = Button(text="Add", width=40, command=save_data)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
