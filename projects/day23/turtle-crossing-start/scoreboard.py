from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-285,260)
        self.level = 1
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f'Level: {self.level}', font=FONT)
    
    def level_up(self):
        self.level +=1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game over.", align="center",font=FONT)
