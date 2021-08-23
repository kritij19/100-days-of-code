from turtle import Turtle

FONT = ('Courier', 15)
ALIGNMENT = 'center'

'''Responsible for the following functionalities:
    1. Displaying the score.
    2. Increasing the score.
    3. Displaying Game over at the centre of the screen'''

# Score is a turtle object.
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        
    def display_score(self):
        self.goto(-20, 270)
        self.write(f"SCORE: {self.score}", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align = ALIGNMENT, font = FONT)
