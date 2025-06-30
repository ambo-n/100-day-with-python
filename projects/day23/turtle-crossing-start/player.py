from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(UP)
        self.penup()
        self.reset_position()
    
    def move_up(self):
        self.forward(MOVE_DISTANCE)
    
    def reset_position(self):
        self.goto(STARTING_POSITION)

    
