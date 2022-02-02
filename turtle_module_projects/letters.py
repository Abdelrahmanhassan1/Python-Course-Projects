import math
import turtle as turtle_module

my_pen = turtle_module.Turtle()

screen = turtle_module.Screen()
screen.bgcolor("#87CEFA")
my_pen.penup()

# Starting position
my_pen.setposition(-303.11, 225.00)
# Ending postion
# my_pen.setposition(300.11, 225.00)

east = 0
north = 90
west = 180
south = 270
my_pen.pensize(10)


def letter_D():
    # Height of 100 and width of 80
    my_pen.pendown()
    my_pen.right(90)
    my_pen.forward(100)
    my_pen.right(-90)
    my_pen.forward(30)
    my_pen.circle(50, 180)
    my_pen.forward(30)
    # Returning the pen to the left right up corner
    my_pen.penup()
    my_pen.seth(0)
    my_pen.forward(110)


def letter_Z():
    # Height of 100 and width of 100
    my_pen.pendown()
    my_pen.forward(100)
    my_pen.right(135)
    my_pen.forward(100*math.sqrt(2))
    my_pen.right(-135)
    my_pen.forward(100)
    # Returning the pen to the left right up corner
    my_pen.penup()
    my_pen.seth(90)
    my_pen.forward(100)
    my_pen.seth(0)
    my_pen.forward(30)


def letter_E():
    # Height of 100 and width of 90
    my_pen.pendown()
    my_pen.forward(75)
    my_pen.penup()
    my_pen.setheading(west)
    my_pen.forward(75)
    my_pen.pendown()
    my_pen.setheading(south)
    my_pen.forward(50)
    my_pen.setheading(east)
    my_pen.forward(50)
    my_pen.penup()
    my_pen.setheading(west)
    my_pen.forward(50)
    my_pen.setheading(south)
    my_pen.pendown()
    my_pen.forward(50)
    my_pen.setheading(east)
    my_pen.forward(75)
    # Returning the pen to the left right up corner
    my_pen.penup()
    my_pen.forward(30)
    my_pen.seth(north)
    my_pen.forward(100)
    my_pen.seth(east)


def letter_F():
    # Height of 100 and width of 90
    my_pen.pendown()
    my_pen.forward(90)
    my_pen.penup()
    my_pen.setheading(west)
    my_pen.forward(90)
    my_pen.pendown()
    my_pen.setheading(south)
    my_pen.forward(50)
    my_pen.setheading(east)
    my_pen.forward(60)
    my_pen.penup()
    my_pen.setheading(west)
    my_pen.forward(60)
    my_pen.setheading(south)
    my_pen.pendown()
    my_pen.forward(50)
    # Returning the pen to the left right up corner
    my_pen.penup()
    my_pen.setheading(east)
    my_pen.forward(90)
    my_pen.forward(30)
    my_pen.seth(north)
    my_pen.forward(100)
    my_pen.seth(east)


def letter_O():
    my_pen.setheading(south)
    my_pen.forward(50)
    my_pen.pendown()
    my_pen.setheading(south)
    my_pen.circle(50)
    # Returning the pen to the left right up corner
    my_pen.penup()
    my_pen.setheading(east)
    my_pen.forward(130)
    my_pen.setheading(north)
    my_pen.forward(50)
    my_pen.setheading(east)


def letter_U():
    my_pen.setheading(south)
    my_pen.pendown()
    my_pen.forward(70)
    my_pen.circle(35, 180)
    my_pen.forward(70)
    # Returning the pen to the left right up corner
    my_pen.penup()
    my_pen.setheading(east)
    my_pen.forward(30)


def letter_J():
    my_pen.setheading(south)
    my_pen.forward(70)
    my_pen.pendown()
    my_pen.circle(35, 180)
    my_pen.forward(70)
    # Returning the pen to the left right up corner
    my_pen.penup()
    my_pen.setheading(east)
    my_pen.forward(30)


letter_J()
letter_U()
letter_E()
letter_O()
# letter_Z()
# letter_D()
# letter_F()
screen.exitonclick()
