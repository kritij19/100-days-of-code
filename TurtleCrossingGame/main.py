from turtle import Screen
from cars import Cars
from myturtle import MyTurtle
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height = 600, width = 600)
# Turns off animation until update called.
screen.tracer(0)

turtle = MyTurtle()
scoreboard = ScoreBoard()
cars = Cars()

screen.listen()
screen.onkey(turtle.move, "Up") 


i = 0   # Incremented in each while loop
game_level = 1 
sleep_time = 0.1  # Loop refresh time
car_limiter = 2   # Limits frequence of creation of cars

# OPTIONAL: displays road
# scoreboard.road()

game_is_on = True

while game_is_on:
    
    screen.update()
    time.sleep(sleep_time)
    
    # Creating cars.
    # Initally a new car is added 1 in every 2 while loops. Beyond level 10, 1 in every while loop.
    if game_level > 10:
        car_limiter = 1
    if i % car_limiter == 0:
        cars.create_car()
        
    # On each iteration moves all cars on screen. Game level controls speed of car.
    cars.move()
   
    # Check if turtle reached the other end
    if  turtle.ycor() >= 240:
        turtle.restart()  # Reset to orginal position
        scoreboard.levelup()
        cars.level_up()
        
        game_level += 1
        sleep_time -= 0.005  # To inc frequency of creation of cars, dec sleep time.
    
    # Detect turtle's collision with car
    for car in cars.all_cars:
        
        # NEEDS IMPROVEMENT
        # Turtle only moves on the y axis, so car can only hit if x coord of car b/w (-20, 20)
        if abs(car.xcor()) < 20 and car.distance(turtle) < 20:
            scoreboard.gameover()
            game_is_on = False
            
            # TESTING
            # print(f'touch with {car.pencolor()}')
            # print(f'distance : {car.distance(turtle)}')
            # print(f' x cor of car: {car.xcor()}')
            # print(f'distance b/w y cor: {abs(car.ycor() - turtle.ycor())}')

    i += 1

screen.exitonclick()
