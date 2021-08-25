from turtle import Turtle,colormode
import random

CAR_LENGTH = 2 # Times 20
CAR_DISTANCE = 10 # Distance car moves in each iteration
DISTANCE_INCREMENT = 5

colormode(255)
def random_rgb():
    r  = random.randint(0, 230)
    g  = random.randint(0, 230)
    b  = random.randint(0, 230)
    return (r, g, b)

'''Capable of performing the following functionalities:
1. Creating cars
2. Moving the cars
3. Increasing speed and clearing all the other cars when as level increases'''

class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()

        self.all_cars = []
        self.carspeed = CAR_DISTANCE

    def create_car(self):
        """Creates random colored car and appends it to the all_cars list."""        
        car = Turtle('square')
        car.shapesize(stretch_len = CAR_LENGTH)
        car.color(random_rgb())
        car.setheading(180)
        car.penup()
        car.speed('fastest')
        
        car.goto(290, random.randint(-240, 240))
        
        self.all_cars.append(car)

    def move(self):
        """Moves the cars by the specified distance"""      
        for car in self.all_cars:
            if car.xcor() > -300:
                car.forward(self.carspeed)
            else:
                car.hideturtle()
    
    def level_up(self):
        """Clears all the previous cars and increases the speed"""  
        self.clear()
        
        for car in self.all_cars:
            car.hideturtle()
        
        self.carspeed += DISTANCE_INCREMENT
        self.all_cars = []
