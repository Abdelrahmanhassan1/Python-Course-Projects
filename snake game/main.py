from turtle import Turtle, Screen
from snake import Snake
import time 

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move_snake()
    screen.listen()
    screen.onkey(snake.move_up,"Up")
    screen.onkey(snake.move_down,"Down")
    screen.onkey(snake.move_right,"Right")
    screen.onkey(snake.move_left,"Left")


screen.exitonclick()