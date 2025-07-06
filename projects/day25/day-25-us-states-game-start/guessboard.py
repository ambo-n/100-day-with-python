from turtle import Turtle
FONT = ("Courier", 12, "normal")

class Guessboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
    
    def update_guessboard(self,x,y,guess):
        self.goto(x,y)
        self.write(guess)
    
    def game_over(self):
        self.goto(0,0)
        self.write("Well done! All states have been guessed!", font=("Courier", 18, "normal"))