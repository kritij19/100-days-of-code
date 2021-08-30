from tkinter import *
from tkinter import PhotoImage
from PIL import ImageTk, Image
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("arial", 20, "italic")
WORD_FONT = ("arial", 45, "bold")
TIME_FOR_FLIP = 3000    # in ms

try:
    # Getting data from csv containing updated list of words (past progress)
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # During first run
    data = pd.read_csv("data/french_words.csv")
else:
    data = pd.read_csv("data/words_to_learn.csv")
finally:
    words_to_learn = data.to_dict(orient = "records")



#---------------------------------------------GENERATE RANDOM FRENCH WORD-------------------------------------------------------#
def generate_word():
    global chosen_dict
    global timer
    global words_to_learn

    # Cancels the previously set timer
    window.after_cancel(timer)

    # Choosing random word from list of available words
    chosen_dict = random.choice(words_to_learn)
    chosen_word = chosen_dict['French']
    
    canvas.itemconfig(canvas_image, image = front_image_final)
    canvas.itemconfig(language, text = "French", fill = 'dimgray')
    canvas.itemconfig(word, text = chosen_word, fill = 'black')

    # After 3 secs flip card
    timer = window.after(TIME_FOR_FLIP, flipcard)

#-----------------------------------------------------FLIP CARD------------------------------------------------------------------#

def flipcard():
    # Replacing prev image with new image
    english_word = chosen_dict['English']
    canvas.itemconfig(canvas_image, image = back_image_final)
    canvas.itemconfig(language, text = "English", fill = "white")
    canvas.itemconfig(word, text = english_word, fill = "white")
    canvas.grid(row = 0, column = 0, columnspan = 2)

#----------------------------------------------------ON RIGHT GUESS----------------------------------------------------------------#   

def on_right_guess():
    print(len(words_to_learn))
    # Removing rightly guessed word and updating csv
    words_to_learn.remove(chosen_dict) # list
    words_to_learn_df = pd.DataFrame(words_to_learn)
    words_to_learn_df.to_csv("data/words_to_learn.csv", index = False)    
    generate_word()

#------------------------------------------------------UI SETUP---------------------------------------------------------------------#
window = Tk()
window.title("Flashcard Game")
window.config(bg = BACKGROUND_COLOR, padx = 25, pady = 25)

# RESIZING: 

# Original size 800 * 526
front_image = Image.open("images\card_front.png")
front_image_resized  = front_image.resize((650, 414), Image.ANTIALIAS)
front_image_final = ImageTk.PhotoImage(front_image_resized)

back_image = Image.open("images\card_back.png")
back_image_resized  = back_image.resize((650, 414), Image.ANTIALIAS)
back_image_final = ImageTk.PhotoImage(back_image_resized)

# original size 100 * 100
tick_image = Image.open(r"images\right.png")
tick_image_resized  = tick_image.resize((85, 85), Image.ANTIALIAS)
tick_image_final = ImageTk.PhotoImage(tick_image_resized)

cross_image = Image.open("images\wrong.png")
cross_image_resized  = cross_image.resize((85, 85), Image.ANTIALIAS)
cross_image_final = ImageTk.PhotoImage(cross_image_resized)

# Canvas setup
canvas = Canvas(width = 650, height = 414, bg = BACKGROUND_COLOR, highlightthickness = 0)
canvas_image = canvas.create_image(325, 212, image = front_image_final)
language = canvas.create_text(325, 120, text = "", fill = 'dimgray', font = LANGUAGE_FONT)
word = canvas.create_text(325, 210, text = "", fill = 'black', font = WORD_FONT)
canvas.grid(row = 0, column = 0, columnspan = 2)

# Tick button
tick_button = Button(image = tick_image_final, highlightthickness = 0, bd = 0, command = on_right_guess)
tick_button.grid(row = 1, column = 1)

# Cross button
cross_button = Button(image = cross_image_final, highlightthickness = 0 , bd = 0, command = generate_word)
cross_button.grid(row = 1, column = 0)

timer = window.after(TIME_FOR_FLIP, flipcard)
# Start with a random word
generate_word()

window.mainloop()
