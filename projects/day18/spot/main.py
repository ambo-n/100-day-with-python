import colorgram,random
import turtle as t

def rgb_colour(r,g,b):
    return (r,g,b)

colors = colorgram.extract('/Users/ambernguyen/Documents/100-day-with-python/projects/day18/spot/image.jpg', 30)
color_list = []
for color in colors:
    color_list.append(rgb_colour(color.rgb.r,color.rgb.g,color.rgb.b))

tim= t.Turtle()
t.colormode(255)
tim.speed(10)
tim.penup()
tim.hideturtle()

dots_per_row =10
dot_spacing = 50
dot_radius =10
grid_size = dots_per_row*dot_spacing

start_x = -grid_size/2 + dot_spacing/2
start_y = -grid_size/2 + dot_spacing/2
for row in range(dots_per_row):
    for col in range(dots_per_row):
        x = start_x + col * dot_spacing
        y = start_y + row * dot_spacing
        tim.goto(x, y)
        tim.dot(dot_radius * 2, random.choice(color_list)) 

screen = t.Screen()
screen.exitonclick()