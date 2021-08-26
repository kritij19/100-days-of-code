from turtle import Turtle, Screen

INITIAL_SNAKE_LENGTH = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

'''Capable of performing the following functions:
    1. Creating the snake
    2. Moving the snake (The snake moves forward unless interuppted)
    3. Changing the direction of the snake (The snake cannot move backward)
    4. Increasing the length of the snake as score increases.
    5. Reseting the snake to original position in original length.'''
    
class Snake:

    def __init__(self):

        # Creating the snake
        turtle_list = []
        self.turtle_list = turtle_list
        
        self.create_snake()
        self.head = turtle_list[0]
        # Update once the snake has been created 
        Screen().update()
    
    def create_snake(self):

        for i in range(INITIAL_SNAKE_LENGTH):
            self.add_segment((-20 * i, 0))

    # Adds a segment to the specified position. Appends a turtle object to the turtle_list.
    def add_segment(self, position):

            self.turtle_list.append(Turtle(shape ='square'))
            self.turtle_list[-1].penup()
            self.turtle_list[-1].color('white')
            self.turtle_list[-1].goto(position)
    
    # Increases length when point scored.Position where added = position of previous tail.
    def increase_length(self):

            self.add_segment(self.turtle_list[-2].position())

    # Moves the last turtle to the second last turtle's position and so on.
    # The first turtle determines the path.
    def move(self):

        turtle_list = self.turtle_list 

        for i in range(len(turtle_list) - 1, 0, -1):
            x = turtle_list[i - 1].xcor()
            y = turtle_list[i - 1].ycor()
            turtle_list[i].goto(x, y)

        self.head.forward(MOVE_DISTANCE)

    # Reseting the snake to original position in original size.
    def reset(self):
        # Current segements off the screen
        for segment in self.turtle_list:
            segment.goto(1000, 1000)
        
        self.turtle_list.clear()
        self.create_snake()
        self.head = self.turtle_list[0]

    # Turning the turtle
    def up(self):

        # The turtle can not move backwards
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):

        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
