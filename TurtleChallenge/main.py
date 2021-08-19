from turtle import Turtle, Screen, colormode
import random

my_turtle = Turtle()
my_turtle.shape("turtle")


''' 1. Square'''
# def square():
#     for i in range(4):
#         my_turtle.right(90)
#         my_turtle.forward(100)

# square()


''' 2. Dashed line'''

# def dashed_line():
 
#     for i in range(5):
#         my_turtle.pendown()
#         my_turtle.forward(10)
#         my_turtle.penup()
#         my_turtle.forward(10)
# dashed_line()

''' 3. To draw randomly colored shapes from triangle(3) to decagon(10) sharing a common edge'''

# colors_list =  ['green yellow', 'salmon', 'rosy brown','medium aquamarine', 'medium purple','cadet blue','dark slate blue']
# for i in range (3,11):
#     color_chosen = random.choice(colors_list)
#     my_turtle.color(color_chosen)
#     for j in range(i):
#         my_turtle.right(360 / i)
#         my_turtle.forward(70)


''' 4. RANDOM WALK WITH RANDOM COLOR'''

# num_list = [1,2,3,4]

# my_turtle.pensize(5)
# my_turtle.speed('fast')
# colormode(255)

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r, g, b) #Tupple of rgb values

# for i in range(100):
#     my_turtle.color(random_color())
#     choice = random.choice(num_list)
#     if choice == 1:
#         my_turtle.forward(20)
#     elif choice == 2:
#         my_turtle.back(20)
#     elif choice ==3:
#         my_turtle.right(90)
#     else:
#         my_turtle.left(90)
    
'''5. Spirograph'''

# colormode(255)

# my_turtle.speed('fastest')

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r, g, b) #Tupple of rgb values
# angle = 0
# for i in range(100):
#     my_turtle.color(random_color())
#     my_turtle.circle(100)
#     my_turtle.right(angle)
#     angle += 0.075


my_screen = Screen()
my_screen.exitonclick()
