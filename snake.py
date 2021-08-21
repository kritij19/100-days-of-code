from tkinter.constants import LEFT
from turtle import Turtle, Screen
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

'''Capable of performing the following functions:
    1.Creating the snake
    2. Moving the snake (The snake moves forward unless interuppted)
    3. Changing the direction of the snake (The snake cannot move backward)'''
    
class Snake:

    def __init__(self):

        # Creating the snake
        turtle_list = []

        for i in range(3):
            turtle_list.append(Turtle(shape ='square'))
            turtle_list[i].penup()
            turtle_list[i].color('white')
            turtle_list[i].goto(-20 * i, 0)
        
        self.turtle_list = turtle_list
        # Update once the snake has been created 
        Screen().update()
    
    def move(self):

        turtle_list = self.turtle_list 

        # Moves the last turtle to the second last turtle's position and so on.
        # The first turtle now determines the path.
        for i in range(len(turtle_list) - 1, 0, -1):
            x = turtle_list[i -1].xcor()
            y = turtle_list[i -1].ycor()
            turtle_list[i].goto(x, y)

        turtle_list[0].forward(MOVE_DISTANCE)

    def up(self):
        # The turtle can not move backwards
        if self.turtle_list[0].heading() != DOWN:
            self.turtle_list[0].setheading(UP)
    
    def down(self):
        if self.turtle_list[0].heading() != UP:
            self.turtle_list[0].setheading(DOWN)
    
    def left(self):
        if self.turtle_list[0].heading() != RIGHT:
            self.turtle_list[0].setheading(LEFT)
    
    def right(self):
        if self.turtle_list[0].heading() != LEFT:
            self.turtle_list[0].setheading(RIGHT)


    
