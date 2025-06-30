from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("Pong")

paddle_1 = Paddle(350,0)
paddle_2 = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddle_1.move_up, "Up")
screen.onkey(paddle_1.move_down, "Down")
screen.onkey(paddle_2.move_up, "w")
screen.onkey(paddle_2.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.current_speed)
    screen.update()
    ball.move()
    # Dectect Collision with wall
    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect collision with paddles
    if ball.distance(paddle_1) <50 and ball.xcor() >320 or ball.distance(paddle_2) <50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.increase_speed()

    # Detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    
        
    print(ball.current_speed)




screen.exitonclick()