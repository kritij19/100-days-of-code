from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()

screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title("SNAKE GAME")
# tracer() turns turtle's animation off until the update function is called.
screen.tracer(0) 

snake = Snake()

game_is_on = True

while game_is_on:
    
    # Update after each movement
    screen.update() 
    # Once updated, sleep for a while so that the snake can be seen in its current state.
    time.sleep(0.1) 

    # Turns
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    # Throughout the game the snake keeps moving.
    snake.move()

screen.exitonclick()  
