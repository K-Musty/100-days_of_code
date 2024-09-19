from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()

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
gen_password_button = Button(text="Generate Password", width=14)
gen_password_button.grid(column=2, row=4)

add_button = Button(text="Add", width=40, command=save_data)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
