import random
import re
from tokenize import maybe
import turtle


from turtle import Turtle, Screen, screensize

my_pen = Turtle()
directions = [0, 90, 180, 270]
my_pen.pensize(10)
my_pen.speed('fastest')


# pen_colors = ["dodger blue", "spring green",
#               "green yellow", "magenta", "medium purple", "hot pink", "light coral", "orange red"]
# instead of using specified colors let's generate some by random
turtle.colormode(255)


def random_color_picker():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    return (red, green, blue)


for _ in range(100):
    my_pen.color(random_color_picker())
    my_pen.forward(30)
    my_pen.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
