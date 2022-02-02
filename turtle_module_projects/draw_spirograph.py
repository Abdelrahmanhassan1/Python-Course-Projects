import turtle as turt
import random

my_pen = turt.Turtle()
turt.colormode(255)
my_pen.speed('fastest')


def random_color_picker():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    return (red, green, blue)


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        my_pen.color(random_color_picker())
        my_pen.circle(100)
        my_pen.setheading(my_pen.heading() + size_of_gap)


draw_spirograph(5)

screen = turt.Screen()
screen.exitonclick()
