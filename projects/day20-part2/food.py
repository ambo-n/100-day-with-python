from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.goto(self.new_position())
    
    def new_position(self):
        x_cor= random.randint(-280,280)
        y_cor= random.randint(-280,280)
        return x_cor, y_cor