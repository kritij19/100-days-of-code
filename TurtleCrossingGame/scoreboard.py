from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 18)

'''Capable of performing the following functionalities:
    1. Displaying level 
    2. Displaying Game over
    3. (Optional: Displaying dotted road)'''

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()   
        self.penup()
        self.goto(-230, 260)
        self.color('black')
        self.level = 1
        self.write(f"LEVEL: {self.level}", align = ALIGNMENT, font = FONT)

    def levelup(self):
        self.clear()
        self.level += 1
        self.write(f"LEVEL: {self.level}", align = ALIGNMENT, font = FONT)
    
    def gameover(self):
        self.goto(0, -260)
        self.write(f"Game Over.", align = ALIGNMENT, font = FONT)
    
    def road(self):
        # Upper border
        self.dotted_line(250)
        # Lower border
        self.dotted_line(-250)
        
    def dotted_line(self, y_cord):
        self.goto(300, y_cord)
        self.setheading(180)
        i = 0
        while self.xcor() > -300:
            if i % 2 == 0:
                self.pendown()
            else:
                self.penup()
            self.forward(10)
            i += 1
