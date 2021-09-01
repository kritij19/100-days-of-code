from tkinter import *
from tkinter import PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('arial', 20, 'italic')

class QuizInterface:

    def __init__(self, quizbrain: QuizBrain): # Input quizbrain of type QuizBrain
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)
        
        tick_image = PhotoImage(file = r'images\true.png')
        cross_image = PhotoImage(file = r'images\false.png')

        self.canvas = Canvas(height = 250, width = 300, bg = 'white', bd = 0, highlightthickness = 0)
        self.que_text = self.canvas.create_text(145,
                                    130, 
                                    text = "Sample text",
                                    width = 280,    # text width
                                    fill = THEME_COLOR, 
                                    font = FONT)
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 50)

        self.tick_button = Button(image = tick_image, bd = 0, highlightthickness = 0, command = self.user_guess_true)
        self.tick_button.config(pady  = 10)
        self.tick_button.grid(row = 2, column = 1)

        self.cross_button = Button(image = cross_image, bd = 0, highlightthickness = 0, command = self.user_guess_false)
        self.cross_button.config(pady = 10)
        self.cross_button.grid(row = 2, column = 0)

        self.score_label = Label(text = "Score: 0", fg = 'white', bg = THEME_COLOR, font = ('arial', 10, 'bold'))
        self.score_label.grid(row = 0, column = 1)

        # First Que
        self.display_next_q()

        self.window.mainloop()

    def display_next_q(self):
        # Bg white when que dispayed
        self.canvas.config(bg = 'white')
        
        if self.quiz.still_has_questions():
            # Displays new question and updates score
            self.score_label.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.que_text, text = q_text)
        else:
            self.canvas.itemconfig(self.que_text, text = "You have reached the end of the quiz.")
            # Disable both buttons 
            self.tick_button.config(state = 'disabled')
            self.cross_button.config(state = 'disabled')
    
    # Check if user's answer is correct
    def user_guess_true(self):
        result = self.quiz.check_answer('True')     # Returns true or false
        self.give_feedback(result)
    
    def user_guess_false(self):
        result = self.quiz.check_answer('False')
        self.give_feedback(result)
    
    # Make the background green/red accordingly and in 1 sec move to next question
    def give_feedback(self, guess_result):
        if guess_result:
            self.canvas.config(bg = 'green')
        else:
            self.canvas.config(bg = 'red')
        
        self.window.after(1000, self.display_next_q)
