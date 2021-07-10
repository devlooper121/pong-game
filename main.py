from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
from decoration import SmartBoard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game!")
screen.tracer(0)

ball = Ball()
score = ScoreBoard()
sb = SmartBoard()
r_paddle = Paddle(370)
l_paddle = Paddle(-370)

screen.listen()

screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")
speed = 0.1
game_on = True
while game_on:
    screen.update()
    time.sleep(speed)
    ball.move()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.y_bounce()

    if ball.distance(r_paddle) <= 70 and ball.xcor() == 350 or ball.distance(l_paddle) <= 70 and ball.xcor() == -350:
        ball.side_bounce()
        sb.combo_strick()
        speed *= 0.9
        sb.clear()
    if ball.xcor() > 390:
        score.l_score()
        sb.resetc()
        ball.ball_service()
        sb.r_part()
        speed = 0.1
    elif ball.xcor() < -390:
        score.r_score()
        sb.resetc()
        ball.ball_service()
        sb.l_part()
        speed = 0.1
