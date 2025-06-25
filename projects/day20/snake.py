from turtle import Turtle

MOVE_DISTANCE =20
X_POSITION = [-40,-20,0]
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.snake=[]
        for x in X_POSITION:
            segment = self.create_segment(x,0)
            self.snake.append(segment)
        self.head = self.snake[0]
    
    def create_segment(self,x,y):
        t= Turtle("square")
        t.color("white")
        t.penup()
        t.goto(x,y)
        return t
    
    def move(self):
        for seg_num in range(len(self.snake)-1,0,-1):
            new_x = self.snake[seg_num-1].xcor()
            new_y = self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(new_x,new_y)
        self.snake[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



