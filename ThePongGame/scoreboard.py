from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 25)
SCORE_COLOR = 'paleturquoise'
WINNER_MSG_COLOR = 'aquamarine'

'''Controls the following functionalities:
    1. Display scores of both paddles
    2. Increase score
    3. Display winner
    4. Display the middle dotted line (additional)'''

class ScoreBoard(Turtle):

    def __init__(self):

        super().__init__(SCORE_COLOR)
        self.color()
        self.hideturtle()
        self.penup()
        
        self.right_score = 0
        self.left_score = 0
        
        self.display_left()
        self.display_right()

    # Dotted line in the middle (Optional).
    def middle_line(self): 
      
        self.color('white')
        self.penup()
        self.goto(0,300)
        self.setheading(270)
        # self.pensize(8)
        for i in range(20):
            if i % 2 == 0:
                self.pendown()
            else:
                self.penup()
            self.forward(30)
            
    # Right score
    def display_right(self):

        self.goto(30, 255)
        self.write(self.right_score, align = ALIGNMENT, font = FONT)
    
    # Left score
    def display_left(self):

        self.goto(-30, 255)
        self.write(self.left_score, align = ALIGNMENT, font = FONT)   

    def increase_score(self, side):
        
        if side == 'right':
                self.right_score += 1    
        else:
            self.left_score += 1
        # Previous score cleared. New score displayed.
        self.clear()
        self.display_right()
        self.display_left()

    def winner(self, winning_side):
        
        self.goto(0,0)
        self.color(WINNER_MSG_COLOR)
       # 'none' on tie
        if winning_side != 'none':
            self.write(f"Game Over. \n{winning_side.upper()} paddle wins.", align = ALIGNMENT, font = FONT)
        else:
            self.write(f"Game Over. \nIts a tie.", align = ALIGNMENT, font = FONT)
