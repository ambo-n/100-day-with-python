from turtle import Turtle

POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT =0

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake = []
        for coordinates in POSITIONS:
            x,y = coordinates
            new_segment = self.create_segment(x,y)
            self.snake.append(new_segment)
        self.snake_head = self.snake[0]
    
    def create_segment(self,x,y):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(x,y)
        return t
    
    def move(self):
        for segment_num in range(len(self.snake)-1,0,-1):
            new_x, new_y = self.snake[segment_num-1].pos()
            self.snake[segment_num].goto(new_x,new_y)
        self.snake_head.forward(20)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
