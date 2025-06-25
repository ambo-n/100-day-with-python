from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
def turn_clockwise():
    tim.tilt(30)

turn_clockwise()
turn_clockwise()
turn_clockwise()
turn_clockwise()
turn_clockwise()
print(tim.tiltangle())
# def move_forward():
#     tim.forward(10)

# def move_backward():
#     tim.backward(10)

# def turn_clockwise():
#     tim.tilt(30)

# screen.listen()
# screen.onkey(key="space", fun=turn_clockwise)
# screen.onkey(key="w", fun=move_forward)
screen.exitonclick()