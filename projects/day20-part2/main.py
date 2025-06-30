from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()