from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list.extend([random.choice(letters) for _ in range(nr_letters)])
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_entry_data = website_entry.get().title()
    username_entry_data = username_entry.get()
    password_entry_data = password_entry.get()
    new_data = {website_entry_data: {
        "email":username_entry_data,
        "password":password_entry_data
    }}
    is_ok = messagebox.askokcancel(title=website_entry_data, message=f"These are the details entered: \nEmail: {username_entry_data} \nPassword: {password_entry_data} \nIs it okay to save?")
    if is_ok:
        if len(website_entry_data) > 0 and len(password_entry_data) > 0:
            try:
                with open("data.json",mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file,indent=4)
            else:
                data.update(new_data)
                with open("data.json",mode="w") as data_file:
                    json.dump(data,data_file, indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
        else:
            messagebox.showinfo(title="Oops",message="Please don't leave any fields empty")
# ---------------------------- SEARCH FUNTION ------------------------------- #
def find_password():
    website = website_entry.get().title()
    if len(website) >0:
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data file found")
        else:
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                pyperclip.copy(password)
                messagebox.showinfo(title=website, message=f"Email: {email}\n\n Password: {password}")
                messagebox.showinfo(message=" Password copied to clipboard!")
            else:
                messagebox.showinfo(title="Error", message="No details for website exists")
    else:
        messagebox.showinfo(title="Empty search",message='Please enter the website you want to search')
        
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

# Labels
website_label = Label(text="Webite:")
website_label.grid(column=0,row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0,row=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

# Entries

website_entry = Entry(width=30)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()

username_entry = Entry(width=38)
username_entry.insert(0, "amber.quynh.nguyen@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2, sticky="w")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

search_button = Button(text="Search",width=12, command=find_password)
search_button.grid(row=1, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


# Image
canvas = Canvas(width=200,height=200)
img_file = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img_file)
canvas.grid(column=1, row=0)


window.mainloop()