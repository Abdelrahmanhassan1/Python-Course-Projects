from turtle import Turtle, Screen
import turtle
my_pen = Turtle()
# change turtle color
my_pen.color("red")
# draw the square
for _ in range(4):
    turtle.delay(50)
    my_pen.fd(100)
    my_pen.right(90)


screen = Screen()
screen.exitonclick()
