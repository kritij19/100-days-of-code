'''HIRST PAINTING: 10 * 10 grid of randomly colored dots of diameter 20 and spacing of 50 '''

from turtle import Turtle, Screen, colormode
import random

'''Extracting the colors'''

# import colorgram
# colors = colorgram.extract('image.jpg',30)
# rgb_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_list.append((r,g,b))

# print(rgb_list)

'''Removing background colors'''

# Numbers with values closer to 255 more whitish, hence removed. Those are most likely the bg colors.
# First 3 values from rgb_list removed.

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

'''Making the Hirst Painting'''

colormode(255)  # Has to imported so that color can be accepted as rgb
my_turtle = Turtle()

my_turtle.speed('fastest')
my_turtle.hideturtle()  # Cursor not visible
my_turtle.penup()   # Lines not visible
i = 0

while i < 10:

    for j in range(9):
        my_turtle.dot(20, random.choice(color_list))
        my_turtle.forward(50)
    
    my_turtle.dot(20, random.choice(color_list))

    # Alternate turns right and left

    if i % 2 != 0 and i < 9:
        my_turtle.right(90)
        my_turtle.forward(30)
        my_turtle.right(90)     
    
    else:
        my_turtle.left(90)
        my_turtle.forward(30)
        my_turtle.left(90)
    i += 1

my_screen = Screen()
my_screen.exitonclick()

