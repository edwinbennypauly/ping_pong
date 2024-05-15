from turtle import  Turtle

class ScorBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.goto(-100,150)
        self.write(self.l_score,align="center",font=("courier", 88 ,"normal"))
        self.goto(100,150)
        self.write(self.r_score,align="center",font=("courier", 88 ,"normal"))

    def refresh(self):
        self.clear()
        self.goto(-100,150)
        self.write(self.l_score,align="center",font=("courier", 88 ,"normal"))
        self.goto(100,150)
        self.write(self.r_score,align="center",font=("courier", 88 ,"normal"))



