import tkinter
import random
from tkinter import messagebox
import pyperclip
import json

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

# ---------------------------- PASSWORD FINDER ------------------------------- #
def search_password():
    page_name = website.get()

    if len(page_name) > 0:
        try:
            with open("data.json") as data_file:
                data_dict = json.load(data_file)
                result = data_dict[page_name]
        except FileNotFoundError:
            messagebox.showinfo(title=page_name, message="No passwords stored for this website")
        except KeyError:
            messagebox.showinfo(title=page_name, message="No passwords stored for this website")
        else:
            messagebox.showinfo(title=page_name, message=f"Email: {result['email']} \nPassword: {result['password']}")
    else:
        messagebox.showinfo(title="No Website Specified", message="Please provide a website to search for.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    page_name = website.get()

    new_data = {
        page_name: {
        "email":user_name.get(),
        "password":password.get()
        }
    }

    if len(page_name) > 0 and len(new_data[page_name]["email"]) > 0 and len(new_data[page_name]["password"]) > 0:
        yes = messagebox.askokcancel(title=page_name, message=f"These are the details entered: \nEmail: {new_data[page_name]['email']} "
                                                           f"\nPassword: {new_data[page_name]['password']} \nIs it ok to save?")
        if yes:
            try:
                with open("data.json") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                data = new_data
            else:
                data.update(new_data)
            finally:
                with open("data.json", 'w') as data_file:
                    json.dump(data, data_file, indent=4)

                    website.delete(0, tkinter.END)
                    password.delete(0, tkinter.END)
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(height=200, width=200)
logo = tkinter.PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

user_name_label = tkinter.Label(text="Email/Username:")
user_name_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

#Inputs
website = tkinter.Entry(width=33)
website.grid(column=1, row=1)
website.focus()

user_name = tkinter.Entry(width=53)
user_name.grid(column=1, row=2, columnspan=2)
user_name.insert(0, MY_EMAIL)

password = tkinter.Entry(width=33)
password.grid(column=1, row=3)

#Buttons
search_button = tkinter.Button(text="Search", command=search_password, width=15)
search_button.grid(column=2, row=1)

add_button = tkinter.Button(text="Add", command=add_password, width=30)
add_button.grid(column=1, row=4, columnspan=2)

get_button = tkinter.Button(text="Generate Password", command=get_password, width=15)
get_button.grid(column=2, row=3)

window.mainloop()