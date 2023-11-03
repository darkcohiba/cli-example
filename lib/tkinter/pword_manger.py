from tkinter import *
from tkinter import messagebox
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password = password_letters + password_symbols + password_numbers
    random.shuffle(password)
    print("".join(password))
    password_entry.delete(0, END)
    password_entry.insert(0, "".join(password))


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    print(f"{website} | {email} | {password}")

    if website and password and email:

        accept = messagebox.askokcancel(title=website,
                                        message=f"These entered details: \nEmail:{email}\nPassword: {password}\nIs it ok to save?")

        if accept:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
    else:
        messagebox.showerror(title="Empty Fields", message="All fields are required")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manger")
window.config(padx=100, pady=100, bg="white")

# canvas with our image
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.grid(row=0, column=1)

logo = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo)

# labels
website_label = Label(text="Website", bg="white", fg="black")
email_label = Label(text="Email/Username", bg="white", fg="black")
password_label = Label(text="password", bg="white", fg="black")
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

# input fields
website_entry = Entry(width=35, fg="black", bg="white", highlightthickness=0, highlightbackground="white")
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35, fg="black", bg="white", highlightthickness=0, highlightbackground="white")
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "email@gmail.com")

password_entry = Entry(width=21, fg="black", bg="white", highlightthickness=0, highlightbackground="white")
password_entry.grid(row=3, column=1)

# buttons
generate_password_button = Button(text="Generate Password", highlightthickness=0, highlightbackground="white",
                                  command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, highlightthickness=0, highlightbackground="white", command=save)
add_button.grid(column=1, row=4, columnspan=2)

# keep the window open
window.mainloop()
