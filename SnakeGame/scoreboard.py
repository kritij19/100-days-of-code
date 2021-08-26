from turtle import Turtle

FONT = ('Courier', 15)
ALIGNMENT = 'center'

'''Responsible for the following functionalities:
    1. Displaying the score.
    2. Increasing the score.
    3. Reseting score to 0 in each game and controlling high score.'''

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()

        # To retain the previous high score
        with open('data.txt',mode = 'r') as file:
            self.highscore = int(file.read())

    # After each game over. Reset score to 0 and change high score if current score greater than prev high score.
    def reset(self):
        if self.score > self.highscore:
                self.highscore = self.score
                # Storing high score in word file so that it's retained.
                # Overwriting the new high score into the file.
                with open('data.txt',mode = 'w') as file:
                    file.write(str(self.highscore))
                
            
        self.display_score()
        self.score = 0
        
    def display_score(self):
        self.clear()
        self.goto(-20, 270)
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.highscore}", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align = ALIGNMENT, font = FONT)
