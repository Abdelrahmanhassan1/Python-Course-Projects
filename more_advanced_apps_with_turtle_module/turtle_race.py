from re import X
import turtle as turt
import random
is_race_on = False
screen = turt.Screen()
screen.setup(width=500, height=400)
user_pet = screen.textinput(title="Choose Your Pet",
                            prompt="Which Turtle will win the race?")

turtle_colors = ["red", "orange", "black", "green", "purple", "blue"]
y_positions = [-80, -50, -20, 10, 40, 70]
turtles_list = []

for turtle_index in range(6):
    new_turtle = turt.Turtle(shape="turtle")
    new_turtle.color(turtle_colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles_list.append(new_turtle)

if user_pet:
    is_race_on = True

while is_race_on:
    for turtle in turtles_list:
        if turtle.xcor() > 230:
            print(f"The Turtle That wins is the ({turtle.pencolor()}) turtle.")
            if user_pet == turtle.pencolor():
                print("Congratulations You WON!!!")
                is_race_on = False
            else:
                print("Sorry, You didn't win!")
                is_race_on = False

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
