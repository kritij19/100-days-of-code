from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()

screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title("SNAKE GAME")
# tracer() turns turtle's animation off until the update function is called.
screen.tracer(0) 

snake = Snake()
food = Food()
score = Score()

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
    score.display_score()
    snake.move()

    # Once snake collides, reset location of food.
    if snake.head.distance(food) < 15:
        food.reset_food()
        score.increase_score()
        snake.increase_length()

    # Detect collision with wall. 
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        print("Boundary touch")
        score.reset()
        snake.reset()
    
    # Detect collision with tail.
    # Slicing since distance between head and head always < 10.
    for turtle in snake.turtle_list[1:]:

        if snake.head.distance(turtle) < 10:
            print("Tail touch")
            score.reset()
            snake.reset()

screen.exitonclick()  
