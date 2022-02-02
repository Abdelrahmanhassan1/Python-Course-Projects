from ctypes.wintypes import RGB
import random
from turtle import Turtle, Screen, screensize
my_pen = Turtle()

# let's draw our shapes:
# for _ in range(4):
#     my_pen.color("red")
#     my_pen.forward(100)
#     my_pen.right(90)

# for _ in range(5):
#     my_pen.color("green")
#     my_pen.forward(100)
#     my_pen.right(72)

# for _ in range(6):
#     my_pen.color("blue")
#     my_pen.forward(100)
#     my_pen.right(60)

# for _ in range(7):
#     my_pen.color("yellow")
#     my_pen.forward(100)
#     my_pen.right(360/7)

# for _ in range(8):
#     my_pen.color("purple")
#     my_pen.forward(100)
#     my_pen.right(45)

# Another Modified Way:
# for number_of_sides in range(4, 11):
#     angle = 360/ number_of_sides
#     for _ in range(number_of_sides):
#         my_pen.color("purple")
#         my_pen.forward(100)
#         my_pen.right(angle)

# or we can create a function to draw a shape given the number of sides

pen_colors = ["dodger blue", "spring green",
              "green yellow", "magenta", "medium purple", "hot pink"]


def draw_geometric_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        # to change every vertex
        # my_pen.color(random.choice(pen_colors))
        my_pen.forward(100)
        my_pen.right(angle)


for sides in range(3, 11):
    my_pen.color(random.choice(pen_colors))
    draw_geometric_shape(sides)


screen = Screen()
screen.exitonclick()
