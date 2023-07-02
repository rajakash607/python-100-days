from turtle import Turtle


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scorecard()

    def update_scorecard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center",
                   font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center",
                   font=("courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scorecard()

    def r_point(self):
        self.r_score += 1
        self.update_scorecard()
