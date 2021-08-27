from tkinter import *

FONT = ('calibri', 12)
SCREEN_SIZE = "250x120"
INPUT_WIDTH = 8

window = Tk()
window.title("Miles to Km Converter")
window.geometry(SCREEN_SIZE)
window.config(padx = 20, pady = 20)

def button_click():
    # get distance in miles
    mile_dist = float(mile_input.get())
    # miles to km
    km_dist = round(mile_dist * 1.609, 3)
    # change km label
    output.config(text = str(km_dist))

# 'is equal to' label
is_equal_to = Label(text = "is equal to", font = FONT)
is_equal_to.grid(row = 1, column = 0)

# miles label 
miles = Label(text = "Miles", font = FONT)
miles.grid(row = 0, column = 2)

# km label
km = Label(text = "Km", font = FONT)
km.grid(row = 1, column = 2)

# mile input
mile_input = Entry(width = INPUT_WIDTH)
mile_input.insert(END, string = '0')
mile_input.grid(row = 0, column = 1)

# Calculate Button
button = Button(text = 'Calculate', command = button_click)
button.grid(row = 2, column = 1)

# km output
output = Label(text = "0", font = FONT)
output.grid(row = 1, column = 1)

window.mainloop()
