from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, paddle_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed(0)
        self.goto(paddle_position[0], paddle_position[1])

    def move_up(self):
        self.sety(self.ycor() + 30)

    def move_down(self):
        self.sety(self.ycor() - 30)

    def reset_position(self, position):
        self.goto(position[0], position[1])
