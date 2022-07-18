from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 350)
        self.color("white")
        self.write("Score: 0", False, align="center",
                   font=("Courier", 24, "normal"))
        self.score = 0

    def update_score(self):
        self.clear()
        self.score += 1
        self.write("Score: {}".format(self.score), False,
                   align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center",
                   font=("Courier", 24, "normal"))
