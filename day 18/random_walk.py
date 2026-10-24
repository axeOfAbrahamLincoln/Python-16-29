import turtle as t
import random




tim = t.Turtle()
tim.shape("turtle")

tim.pen(pensize=6, speed=10)

def random_move():
    tim.color(random.random(),random.random(),random.random())
    random_direction = random.choice([0,90,180,270])
    tim.setheading(random_direction)
    tim.fd(15)
    

for _ in range(100):
    random_move()


















screen = t.Screen()
screen.exitonclick()