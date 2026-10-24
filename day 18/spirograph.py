import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.speed(6)
angle = 0

while angle <= 360:
    tim.color(random.random(),random.random(),random.random())
    tim.circle(80)
    angle +=5
    tim.setheading(angle)
    



screen = t.Screen()
screen.exitonclick()