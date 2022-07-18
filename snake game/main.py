from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()
    # detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh_food_location()
        snake.extend()
        scoreboard.update_score()

    # detect collision with wall
    if snake.snake_head.xcor() > 390 or snake.snake_head.xcor() < -390 or snake.snake_head.ycor() > 390 or snake.snake_head.ycor() < -390:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with itself
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
