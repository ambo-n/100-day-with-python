from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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
    website_entry_data = website_entry.get()
    username_entry_data = username_entry.get()
    password_entry_data = password_entry.get()
    is_ok = messagebox.askokcancel(title=website_entry_data, message=f"These are the details entered: \nEmail: {username_entry_data} \nPassword: {password_entry_data} \nIs it okay to save?")
    if is_ok:
        if len(website_entry_data) > 0 and len(password_entry_data) > 0:
            with open("data.txt",mode="a") as manager_file:
                manager_file.write(f"{website_entry_data} | {username_entry_data} | {password_entry_data} \n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)
        else:
            messagebox.showinfo(title="Oops",message="Please don't leave any fields empty")
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

website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=38)
username_entry.insert(0, "amber.quynh.nguyen@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


# Image
canvas = Canvas(width=200,height=200)
img_file = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img_file)
canvas.grid(column=1, row=0)


window.mainloop()