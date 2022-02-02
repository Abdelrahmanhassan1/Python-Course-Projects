from color_extractor_from_image import extract_color
import turtle as turtle_module
import random
my_pen = turtle_module.Turtle()
# my_pen.speed('fastest')
turtle_module.colormode(255)
rgb_colors = extract_color('hist_spot_painting.jpg')

screen = turtle_module.Screen()
screen.bgcolor("#87CEFA")
my_pen.penup()
# my_pen.hideturtle()

def draw_spots_raw(number_of_dots):
    for dot_count in range(1, number_of_dots+1):
        my_pen.dot(40, random.choice(rgb_colors))
        my_pen.forward(50)
        if dot_count % 10 == 0:
            my_pen.setheading(90)
            my_pen.forward(50)
            my_pen.setheading(180)
            my_pen.forward(500)
            my_pen.setheading(0)


# start the first row location
my_pen.setheading(225)
my_pen.forward(340)
my_pen.setheading(0)

draw_spots_raw(100)


screen.exitonclick()
