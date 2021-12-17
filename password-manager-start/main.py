import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for item in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for item in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for item in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Missing Info Error", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Missing data.json file", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Website not found.", message=f"There was no details for {website}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
# window.minsize(width= 500, height= 300)
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=22)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "powershot2032@gmail.com")
password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
search_button = Button(text="Search", width=13 ,command=find_password)
search_button.grid(row=1, column=2)
add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()