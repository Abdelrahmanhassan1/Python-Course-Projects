from turtle import Turtle, Screen
my_pen = Turtle()

# Draw dash line


def draw_dash_line():
    for _ in range(5):
        my_pen.forward(20)
        my_pen.penup()
        my_pen.forward(20)
        my_pen.pendown()


for _ in range(4):
    draw_dash_line()
    my_pen.right(90)

screen = Screen()
screen.exitonclick()
