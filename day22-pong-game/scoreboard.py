
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.write("Left Player: 0 , Right Player: 0", align="center",
                   font=("Courier", 20, "normal"))
        self.left_score = 0
        self.right_score = 0

    def update_score(self, left_score, right_score):
        self.left_score += left_score
        self.right_score += right_score
        self.clear()
        self.write("Left Player: {} , Right Player: {}".format(
            self.left_score, self.right_score), align="center", font=("Courier", 20, "normal"))
