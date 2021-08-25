from turtle import Turtle

STEP_SIZE = 20
STARTING_POSITION = (0, -280)

'''Capable of performing the following functionalities:
    1. Creating turtle and placing at starting position
    2. Moving the turtle up
    3. Resetting turtle to original position.'''

class MyTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('Black')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90) 
        self.speed('fast')
        
    def move(self):
        self.forward(STEP_SIZE)
    
    def restart(self):
        self.clear()
        self.goto(STARTING_POSITION)
