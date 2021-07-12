# imorts
from turtle import textinput, Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
from decoration import SmartBoard
import time

# turtle screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game!")

# welcome msg
wmsg = textinput("Welcome to The Classic Pong Game", "\nDo you want play the game ? [y/n]")
game_on = True
if wmsg != "y":
    game_on = False

def quit_game():
    """quit game"""
    screen.bye()

screen.tracer(0)

# variables
ball = Ball()
score = ScoreBoard()
sb = SmartBoard()

# left and right paddle from Paddle class
r_paddle = Paddle(370)
l_paddle = Paddle(-370)

# key events
screen.listen()

screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")
screen.onkey(fun=quit_game, key="q")
screen.onkey(fun=ball.play_pause , key="space")

speed = 0.1
game_on = True
while game_on:
    screen.update()
    time.sleep(speed)
    ball.move()

    # collision with upper and lower wall 
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.y_bounce()

    # hit by any paddle
    if ball.distance(r_paddle) <= 70 and ball.xcor() == 350 or ball.distance(l_paddle) <= 70 and ball.xcor() == -350:
        ball.side_bounce()
        sb.combo_strick()
        speed *= 0.9 # for increasing speed by decreasing sleep time
        sb.clear()

    # if miss right opaddle, or left paddle
    if ball.xcor() > 390:
        score.l_score()
        sb.resetc()
        ball.ball_service()
        sb.r_part()
        speed = 0.1 # reset speed after each miss
    elif ball.xcor() < -390:
        score.r_score()
        sb.resetc()
        ball.ball_service()
        sb.l_part()
        speed = 0.1 # reset speed after each miss
