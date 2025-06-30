from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_SPEED = 0.1


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        # self.x_pos = random.randint(-300,300)
        self.y_pos = random.randint(-250,250)
        self.goto(300,self.y_pos)
        self.car_speed = CAR_SPEED
    
    def move(self):
        self.forward(MOVE_INCREMENT)
    

