from turtle import Turtle, Screen
import random
colours = ["red", "orange","yellow","green","blue","purple"]

screen = Screen()
screen.setup(width=500,height=400)

def make_a_race_turtle(x,y,colour):
    t= Turtle(shape="turtle")
    t.penup()
    t.goto(x=x,y=y)
    t.color(colour)
    return t

all_turtles =[]
y_positions =[-150,-90,-30,30,90,150]

for i in range(6):
    new_turtle = make_a_race_turtle(-230, y_positions[i], colours[i])
    all_turtles.append(new_turtle)

user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner")
            else:
                print(f"You lost! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()