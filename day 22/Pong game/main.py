from turtle import Screen
from padle import Padle
from ball import Ball
from scoreboard import Scoreboard
from intro import Intro
import time

player1 = (350, 0)
player2 = (-350, 0)
player1_name = "P1"
player2_name = "P2"

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


def start_game():
    r_padle = Padle(player1, player1_name)
    l_padle = Padle(player2, player2_name)
    ball = Ball()
    score = Scoreboard()

    screen.listen()
    screen.onkey(r_padle.up, "Up")
    screen.onkey(r_padle.down, "Down")
    screen.onkey(l_padle.up, "w")
    screen.onkey(l_padle.down, "s")

    game_on = True

    while game_on:
        time.sleep(ball.move_speed)
        r_padle.update_label()
        l_padle.update_label()
        screen.update()
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if (ball.xcor() > 320 and ball.distance(r_padle) < 50) or \
           (ball.xcor() < -320 and ball.distance(l_padle) < 50):
            ball.bounce_x()

        if ball.xcor() > 380:
            ball.restart()
            score.l_score_increase()
            score.update_scoreboard()

        if ball.xcor() < -380:
            ball.restart()
            score.r_score_increase()
            score.update_scoreboard()


        if score.l_score == 5:
            score.game_over(player2_name)
            game_on = False

        if score.r_score == 5:
            score.game_over(player1_name)
            game_on = False


# SHOW INTRO FIRST
Intro(start_game)

screen.mainloop()