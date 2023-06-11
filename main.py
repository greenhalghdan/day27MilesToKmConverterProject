from tkinter import *

result = 0

def convert_miles_to_km():
    resultlabel.config(text=int(input.get())*1.609344)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)
# labels:

mileslabel = Label(text="Miles")
kmlabel = Label(text="Is equal to")
resultlabel = Label(text=result)
mileslabel.grid(column=2, row=0)
kmlabel.grid(column=0, row=1)
resultlabel.grid(column=1, row=1)

# Data Entry

input = Entry(width=10)
input.insert(END, "0")
input.focus()
input.grid(column=1, row=0)

#buttons

convert = Button(text="Calculate", command=convert_miles_to_km)
convert.grid(column=1, row=2)
window.mainloop()