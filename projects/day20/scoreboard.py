from turtle import Turtle
ALIGNMENT ="center"
FONT =("courier", 25, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.score =0
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)
        
    
    def update_score(self):
        self.clear()
        self.score +=1
        self.write(f"Score: {self.score} ", align='center', font=("courier", 25, 'normal'))
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)

