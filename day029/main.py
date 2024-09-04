import random
import string
import tkinter as tk
from tkinter import messagebox

import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(15))
    pyperclip.copy(password)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(
            title="Oops", message="Please don't leave any fields empty!"
        )
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: \n\nEmail: {email}\nWebsite: {website}\nPassword: {password}\n\nIs it ok to save?",
    )

    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")

        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(130, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
pasword_label = tk.Label(text="Password:")
pasword_label.grid(column=0, row=3)

website_entry = tk.Entry(width=39)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = tk.Entry(width=39)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "kek@kek.com")
password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password_btn = tk.Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3)
add_btn = tk.Button(text="Add", width=37, command=save)
add_btn.grid(column=1, row=4, columnspan=2)


# ---------------------------- CENTERING WINDOW ------------------------------- #
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()
