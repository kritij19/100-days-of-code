from turtle import Turtle, colormode
import random

colormode(255)
food_shapes = ['circle','square']

# Random color of food. Food should be visible hence rgb range between 150 and 255.
def random_rgb():
    r = random.randint(150, 255)
    g = random.randint(150, 255)
    b = random.randint(150, 255)
    return (r,g,b)

'''Food class inherits from the turtle class. All methods of turtle can now be directly used.
   Food itself is also a turtle object.
   Fuunctionalities:
   1. Resets food at random locations'''

class Food(Turtle):

    # All methods implemented as soon as a food object is created.
    def __init__(self):
      
        super().__init__()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.penup()
        # Random location for first food object.
        self.reset_food() 

    # Resets food at a new random location.
    def reset_food(self):
      
        self.color(random_rgb())
        self.shape(random.choice(food_shapes))
        x = random.randint(-280, 280)
        # Food should appear beloww the scoreboard.
        y = random.randint(-280, 260)
        self.goto(x, y)

