from turtle import *


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position, 0)

    def up(self):
        self.goto(self.xcor(), self.ycor()+30)

    def down(self):
        self.goto(self.xcor(), self.ycor()-30)
