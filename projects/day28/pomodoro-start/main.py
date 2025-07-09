from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer =0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks["text"] = ""

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    # work_sec = 15
    # short_break_sec = 5
    # long_break_sec = 10
    if reps %8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps, timer
    count_min = math.floor(count/60)
    count_sec = count%60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02}")
    if count >0:
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks =""
        for _ in range(math.floor(reps/2)):
            marks += "✓"
        check_marks["text"] = marks


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#Label
title_label = Label(text="Timer", font=(FONT_NAME, 45, "normal"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

check_marks = Label(font=(FONT_NAME, 30, "normal"), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1,row=3)

# Button
start_button = Button(text="Start", command=start_timer)
# start_button.config(padx=0,pady=0, borderwidth=0, relief="flat")
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2,row=2)

# Tomato
canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="/Users/ambernguyen/Documents/100-day-with-python/projects/day28/pomodoro-start/tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35, "bold"))
canvas.grid(column=1, row=1)





window.mainloop()