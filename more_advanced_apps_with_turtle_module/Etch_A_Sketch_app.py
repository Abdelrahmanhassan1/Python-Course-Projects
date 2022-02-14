import turtle as turt

my_pen = turt.Turtle()
screen = turt.Screen()
screen.bgcolor("spring green")
my_pen.pensize(5)

east = 0
north = 90
west = 180
south = 270


def move_forwards():
    my_pen.forward(10)


def move_backwards():
    my_pen.backward(10)


def turn_right():
    my_pen.setheading(my_pen.heading() - 10)


def turn_left():
    my_pen.setheading(my_pen.heading() + 10)


def clear():
    my_pen.clear()
    my_pen.penup()
    my_pen.home()
    my_pen.pendown()


screen.listen()
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="r", fun=clear)


screen.exitonclick()
