from tkinter import *

def convert_miles_to_km():
    miles = input.get()
    miles_to_km = float(miles)*1.609
    result["text"] = miles_to_km

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20,pady=20)

# Entry
input = Entry(width=7)
input.insert(END, string="0")
input.grid(column=1,row=0)
#Labels
text= Label(text="is equal to")
text.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

result = Label(text="0")
result.grid(column=1, row=1)

# Button
button = Button(text="Calculate",command=convert_miles_to_km)
button.grid(column=1, row=2)


window.mainloop()