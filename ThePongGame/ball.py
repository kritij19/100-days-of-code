from turtle import Turtle
# Speed of the ball can be increased by increasing x and y moving distances.
Y_MOVING_DISTANCE = 10
X_MOVING_DISTANCE = 10
# Speed increase with each successive score.
SPEED_INCREASE = 3
BALL_COLOR = 'paleturquoise'

'''Controls the following functionalities:
    1. Making the ball.
    2. Movement of the ball.
    3. Reflection of the ball on collision with wall and paddle.
    4. Reseting ball to centre when it goes out of bounds.
    5. Increasing speed of ball on each score increase.'''

class Ball(Turtle):

    def __init__(self) :
        
        super().__init__()
        self.shape('circle')
        self.color(BALL_COLOR)
        self.penup()
        
        self.y_increment = Y_MOVING_DISTANCE
        self.x_increment = X_MOVING_DISTANCE

    # Increment the x and y coordinate according to the amount specified.
    def move(self):
        self.setx(self.xcor() + self.x_increment)
        self.sety(self.ycor() + self.y_increment)

    # Inverts the direction of motion in the y direction.
    def reflect_wall(self):      
        self.y_increment *= -1 

    # Inverts the direction of motion in the x direction.
    def reflect_paddle(self):      
        self.x_increment *= -1 
    
    # Resets ball to centre. Ball now moves towards opp paddle (inverts motion in x).
    def reset(self):      
        self.goto(0, 0)
        self.x_increment *= -1

    # Inceases the speed by certain amount
    def increase_speed(self):  
        self.y_increment += SPEED_INCREASE
        self.x_increment += SPEED_INCREASE

