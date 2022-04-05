import tkinter
import random
from tkinter import messagebox
import pyperclip

MY_EMAIL = "myemail@gmail.com"  #change to user's default email
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
CHARS = ['!', '@', '#', '%', '/', '*', '&', '^', '+', ')', '(']
NUMS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def get_password():
    pass_list = [random.choice(LETTERS) for _ in range(random.randint(8, 12))]
    pass_list += [random.choice(CHARS) for _ in range(random.randint(2, 4))]
    pass_list += [random.choice(NUMS) for _ in range(random.randint(2, 4))]

    random.shuffle(pass_list)
    pass_string = "".join(pass_list)

    pyperclip.copy(pass_string)
    password.delete(0, tkinter.END)
    password.insert(0, pass_string)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    if len(website.get()) > 0 and len(user_name.get()) > 0 and len(password.get()) > 0:
        yes = messagebox.askokcancel(title=website.get(), message=f"These are the details entered: \nEmail: {user_name.get()} "
                                                           f"\nPassword: {password.get()} \nIs it ok to save?")
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    if yes:
        try:
            with open("passwords.txt", mode='a') as file:
                file.write(f"{website.get()} | {user_name.get()} | {password.get()}\n")
                website.delete(0, tkinter.END)
                password.delete(0, tkinter.END)
        except FileNotFoundError:
            with open("passwords.txt", mode='w') as file:
                file.write(f"{website.get()} | {user_name.get()} | {password.get()}\n")
                website.delete(0, tkinter.END)
                password.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(height=200, width=200)
logo = tkinter.PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Inputs
website = tkinter.Entry(width=53)
website.grid(column=1, row=1, columnspan=2)
website.focus()

user_name = tkinter.Entry(width=53)
user_name.grid(column=1, row=2, columnspan=2)
user_name.insert(0, MY_EMAIL)

password = tkinter.Entry(width=33)
password.grid(column=1, row=3)

#Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

user_name_label = tkinter.Label(text="Email/Username:")
user_name_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

#Buttons
add_button = tkinter.Button(text="Add", command=add_password, width=30)
add_button.grid(column=1, row=4, columnspan=2)

get_button = tkinter.Button(text="Generate Password", command=get_password, width=15)
get_button.grid(column=2, row=3)

window.mainloop()