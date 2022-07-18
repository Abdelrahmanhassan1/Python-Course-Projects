import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        # self will be for the turtle class === Turtle.shape("cirlce")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh_food_location()

    def refresh_food_location(self):
        # note that we are having the screen size 600 * 600
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
