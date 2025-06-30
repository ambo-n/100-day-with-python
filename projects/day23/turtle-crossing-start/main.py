import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
scoreboard = Scoreboard()

list_of_cars =[]
first_car = CarManager()
list_of_cars.append(first_car)

car_speed =0.1

screen.listen()
screen.onkey(tim.move_up,'Up')

number_of_loops =0

game_is_on = True
while game_is_on:
    time.sleep(car_speed)
    screen.update()
    number_of_loops +=1
    if number_of_loops%6 ==0:
        car = CarManager()
        list_of_cars.append(car)
    for car in list_of_cars:
        car.move()
        if car.distance(tim) < 25:
            scoreboard.game_over()
            game_is_on = False
    if tim.ycor() == 280:
        tim.reset_position()
        scoreboard.level_up()
        car_speed *= 0.6
    

screen.exitonclick()