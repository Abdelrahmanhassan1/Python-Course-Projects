from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
# to turn off the animations
screen.tracer(0)

right_paddle = Paddle((350, 10))
left_paddle = Paddle((-350, -10))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_vertical()

    # detect collision with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_horizontal()

    # detect collision with the right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        right_paddle.reset_position((350, 10))
        left_paddle.reset_position((-350, -10))
        scoreboard.update_score(1, 0)

    # detect collision with the left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        left_paddle.reset_position((-350, 10))
        right_paddle.reset_position((350, -10))
        scoreboard.update_score(0, 1)


screen.exitonclick()
