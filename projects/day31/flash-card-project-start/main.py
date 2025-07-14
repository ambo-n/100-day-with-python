from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
current_card ={}
to_learn={}

# -----------------WORDS TO DISPLAY------------------
try:
    data_file = pd.read_csv("flash-card-project-start/data/words_to_learn.csv")
except FileNotFoundError:
    data_file = pd.read_csv("flash-card-project-start/data/french_words.csv")

to_learn = data_file.to_dict('records')

def next_card():
    global current_card, timer
    window.after_cancel(timer)
    canvas.itemconfig(flash_card, image = card_front_image)
    current_card= random.choice(to_learn)
    canvas.itemconfig(card_word, text=f"{current_card['French']}", fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    timer = window.after(3000,flip_card)
    

def flip_card():
    canvas.itemconfig(flash_card, image=card_back_image)
    canvas.itemconfig(card_word, text=f"{current_card['English']}", fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")

def is_known():
    to_learn.remove(current_card)
    df = pd.DataFrame(to_learn)
    df.to_csv("flash-card-project-start/data/words_to_learn.csv", index=False)


# -----------------UI SETUP------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)


# Button
cross_image = PhotoImage(file="flash-card-project-start/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0,border=0, command=next_card)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file="flash-card-project-start/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, border=0, command=lambda: [is_known(), next_card()])
known_button.grid(row=1,column=1)

# Canvas

canvas = Canvas(width=800,height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_image = PhotoImage(file="flash-card-project-start/images/card_front.png")
card_back_image = PhotoImage(file="flash-card-project-start/images/card_back.png")
flash_card = canvas.create_image(400,263,image=card_front_image)
card_title = canvas.create_text(400,150, text="", fill="black", font=LANGUAGE_FONT)
card_word = canvas.create_text(400,263, text="", fill="black", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

next_card()



window.mainloop()