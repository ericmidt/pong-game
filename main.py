from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_r.move_up, "Up")
screen.onkeypress(paddle_r.move_down, "Down")
screen.onkeypress(paddle_l.move_up, "w")
screen.onkeypress(paddle_l.move_down, "s")

speed = 0.1
direction = 1
game_over = False
while not game_over:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect collision with the right paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 and ball.x_move > 0:
        ball.bounce_x()

    # Detect collision with the left paddle
    if ball.distance(paddle_l) < 50 and ball.xcor() < -320 and ball.x_move < 0:
        ball.bounce_x()

    # Detect if ball goes out of bound on the right
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if ball goes out of bound on the left
    if ball.xcor() < -395:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
