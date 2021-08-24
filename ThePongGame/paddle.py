from turtle import Turtle

# Speed of the paddle can be adjusted by adjusting the move distance. 
MOVE_DISTANCE = 20

'''Controls the following functionalities:
    1. Making the paddles
    2. Moving the paddles.'''

class Paddle(Turtle):

    def __init__(self, location = (0,0)) :
        super().__init__()
        self.location = location
        
        # Initial sqaure size = 20 * 20
        self.shape('square')
        self.color('white')
        self.penup()
        # Paddle size: 100 * 20
        self.shapesize(stretch_len = 5)
        self.setheading(90)
        self.goto(self.location)
    
    def up(self):
        self.forward(MOVE_DISTANCE)
    
    def down(self):
        self.backward(MOVE_DISTANCE)
    
