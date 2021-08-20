'''To implement the following controls for the turtle from the keyboard-
w: forward
s: backward, 
d: rotates clockwise, 
a: rotates anticlockwise 
c: cleares screen
The turtle draws while it moves'''

from turtle import Turtle, Screen

my_turtle = Turtle()

def move_forward():
  my_turtle.forward(10)

def move_backward():
  my_turtle.backward(10)

def turn_clockwise():
  my_turtle.right(10)

def turn_anticlockwise():
  my_turtle.left(10)

def turtle_reset():
  my_turtle.reset()

my_screen = Screen()

#Making the turtle implement the action that is intended from the keyboard.
my_screen.listen()
my_screen.onkey(move_forward, "w")
my_screen.onkey(move_backward, "s")
my_screen.onkey(turn_clockwise, "d")
my_screen.onkey(turn_anticlockwise, "a")
my_screen.onkey(turtle_reset, "c")


my_screen.exitonclick()
