from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# Score at which game ends, winner declared.
WINNER_SCORE = 10

screen  = Screen()
screen.setup(height = 600, width = 800)
screen.bgcolor('black')
screen.title("The Pong Game")
# Turn off animation while paddle, screen are being setup.
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
# The right paddle controlled by the: Up and down keys
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

# The left paddle controlled by the: w and s keys
screen.onkey(left_paddle.down, "s")
screen.onkey(left_paddle.up, "w")

# The screen needs to be continuously updated.
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    # scoreboard.middle_line()
    ball.move()
    ball.speed('fastest')

    # Detect collision with upper and lower walls
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.reflect_wall()

    # Detect collision with paddle
    # Absolute difference between y coordinates can hit either above or below the middle of the board. 
    # Not reflected if hits the edge. Should hit the front.
    if right_paddle.xcor() - ball.xcor() <= 20 and right_paddle.xcor() - ball.xcor() >= 15 and abs(ball.ycor() - right_paddle.ycor())  <= 50:
        ball.reflect_paddle()

    if ball.xcor() - left_paddle.xcor() <= 20 and ball.xcor() - left_paddle.xcor() >= 15 and  abs(ball.ycor() - left_paddle.ycor())  <= 50:
        ball.reflect_paddle()

    # If right paddle misses
    if ball.xcor() > 360 :
        # Ball reset. Moves towards opposite direction now.
        ball.reset()
        scoreboard.increase_score(side = 'left')
        ball.increase_speed()
    
    # If left paddle misses.
    if ball.xcor() < -360:
        ball.reset()
        scoreboard.increase_score(side = 'right')
        ball.increase_speed()

    # Condition of game over
    # Right wins
    if scoreboard.right_score == WINNER_SCORE and scoreboard.left_score != WINNER_SCORE:
        game_is_on = False
        # Increment score of other paddle when ball goes out of bounds for this.
        scoreboard.winner(winning_side = 'right')
    # Left wins
    elif scoreboard.right_score != WINNER_SCORE and scoreboard.left_score == WINNER_SCORE:
        game_is_on = False
        scoreboard.winner(winning_side = 'left')
    # Tie
    elif scoreboard.right_score == WINNER_SCORE and scoreboard.left_score == WINNER_SCORE:
        game_is_on = False
        scoreboard.winner(winning_side = 'none')

screen.exitonclick()
