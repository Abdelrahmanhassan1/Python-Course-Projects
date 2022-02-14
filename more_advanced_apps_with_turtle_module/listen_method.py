import turtle as turt

my_pen = turt.Turtle()
screen = turt.Screen()
screen.bgcolor("spring green")
my_pen.pensize(5)

east = 0
north = 90
west = 180
south = 270


def move_forward():
    my_pen.setheading(east)
    my_pen.forward(10)


def move_backward():
    my_pen.setheading(west)
    my_pen.forward(10)


def move_up():
    my_pen.setheading(north)
    my_pen.forward(10)


def move_down():
    my_pen.setheading(south)
    my_pen.forward(10)


screen.listen()
screen.onkey(key="Right", fun=move_forward)
screen.onkey(key="Left", fun=move_backward)
screen.onkey(key="Up", fun=move_up)
screen.onkey(key="Down", fun=move_down)


screen.exitonclick()
