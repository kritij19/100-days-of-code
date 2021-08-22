from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width = 500, height = 400)

color_list = ['red', 'yellow', 'orange', 'green', 'blue','purple']
# To hold all the turtle objects
turtle_list = [] 


# Creating and positioning the 6 turtles

for i in range(6):
  turtle_list.append(Turtle(shape = 'turtle')) 
  turtle_list[i].penup()
  turtle_list[i].speed('fast')
  # Set diff color for each of the turtles
  turtle_list[i].color(color_list[i]) 
  # Position the turtles
  y = -100 + 40 * i
  turtle_list[i].goto(-230, y) 


# Prompting the user to place their bet on one of the turtles

user_bet = my_screen.textinput(title = "Make your bet", prompt = "Type the color of the turtle on which you'd like to place your bet")

race_is_on = False

# Ensures that race only starts when the bet has been placed. Returns true if user_bet exists.
if user_bet:
    race_is_on = True

while race_is_on:

    for turtle_obj in turtle_list:

        # Identifying the winner
        # Ensure that the race stops once one of the turtles crosses the finish line
        if turtle_obj.xcor() > 230: 
            race_is_on = False 
            if user_bet == turtle_obj.pencolor():
                print("You win!")
            else:
                print("You lose!")
            print(f"The color of the winning turtle is {turtle_obj.pencolor()}")

        # Making the turtles move a random distance in each step
        step = random.randint(0,10)
        turtle_obj.forward(step)

my_screen.exitonclick()
