# def add(*args):
#     total=0
#     for num in args:
#         total += num
#     return total

# print(add(1,2,3,4,5))

from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a label", font=("Arial",24,"bold"))
my_label.grid(column=0, row=0)

# Button

def button_clicked():
    print("I got clicked")
    text= get_input()
    my_label["text"] = text

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button_2 = Button(text="Don't click")
button_2.grid(column=2,row=0)
# Entry
input = Entry()
input.grid(column=3, row=3)

def get_input():
    return input.get()

window.mainloop()