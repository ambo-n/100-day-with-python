from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)


# Image
canvas = Canvas(width=200,height=200)
img_file = PhotoImage(file="/Users/ambernguyen/Documents/100-day-with-python/projects/day29/password-manager-start/logo.png")
canvas.create_image(100,100,image=img_file)
canvas.grid(column=1, row=0)


window.mainloop()