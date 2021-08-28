'''POMODORO TECHNIQUE: Sets a timer for the following routine:
                        25 min work- 5 min break
                        25 min work- 5 min break
                        25 min work- 5 min break
                        25 min work- 20 min break'''

from tkinter import *

# ----------------------------------- CONSTANTS ------------------------------------ #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
cycle = 0
checkmark_string = ""
clock = None

# --------------------------------- TIMER RESET ------------------------------------ # 

def reset_timer():
    """Resets timer to 0. Sets cycle to 0 and checkmark string to an empty string."""
    
    global cycle
    global checkmark_string
    # Stops the clock
    window.after_cancel(clock)
    cycle = 0
    checkmark_string = " "
    # Reset timer label text to default i.e. "Timer"
    timer.config(text = "Timer") 
    canvas.itemconfig(timer_text, text = "00:00")
    checkmark.config(text = "")


# --------------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    """Controls functioning of the timer. Decides which task to be performed at a specific time.
        Calls the countdown function for the time designated for that specific task.."""
    global cycle
    global checkmark_string
    
    cycle += 1
    # Last break long break
    if cycle == 8:
        timer.config(text = "Break", fg = RED )
        count_down(LONG_BREAK_MIN * 60)
    elif cycle % 2 == 0:
        timer.config(text = "Break", fg = PINK )
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer.config(text = "Work", fg = GREEN )
        count_down(WORK_MIN * 60)
    
    # Checkmark to be displayed after every work cycle i.e. When the break starts.
    if cycle > 1 and cycle % 2 == 0:
        checkmark_string += "✔"
        checkmark.config(text = checkmark_string)



# -------------------------------- COUNTDOWN MECHANISM -------------------------------------- # 

# Cannot use a while loop inside mainloop.

def count_down(count):
    """"Controls time display. Recursive function calling itself each time with a decreased input.
        Input is total time in seconds."""
    global clock

    minutes = int(count / 60)
    seconds = count % 60
    
    if seconds < 10:
        seconds = "0" + str(seconds)
        
    if count >= 0:
        # .after() implements function after given time intervals
        # Time in ms, func, Input to be passed into the func
        clock = window.after(1000, count_down, count - 1)
        canvas.itemconfig(timer_text, text = f"{minutes}:{seconds}")
    else:
        # Once done with one whole task timer now sets countdown to next task.
        start_timer()
    
# ---------------------------- UI SETUP ----------------------------------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

# Putting the image on the screen

# Canvas obj with dimension of img
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)  
tomato_img = PhotoImage(file = 'tomato.png')
canvas.create_image(100, 112, image = tomato_img)   # Takes only PhotoImage object as input
timer_text = canvas.create_text(106, 132, text = "00:00", fill = 'white',font = (FONT_NAME, 30, 'bold'))
canvas.grid(row = 1,column = 1) 

# "TIMER" label
timer = Label(text = "Timer", font = (FONT_NAME, 32, 'bold'), fg = GREEN, bg = YELLOW)
timer.grid(row = 0,column = 1)


# START button
start_button = Button(text = "Start", bg = 'white', command = start_timer)
start_button.grid(row = 2, column = 0)

# RESET button
reset_button = Button(text = "Reset", bg = 'white', command = reset_timer)
reset_button.grid(row = 2, column = 2)

# CHECKMARK
checkmark = Label(text = " ", font = (FONT_NAME, 15),fg = GREEN, bg = YELLOW)
checkmark.grid(row = 3, column = 1)

window.mainloop()
