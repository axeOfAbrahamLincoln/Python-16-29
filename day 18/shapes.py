from turtle import Turtle, Screen
import random



tim = Turtle()
tim.shape("turtle")
tim.color("VioletRed1")

shape_sides = 3

while shape_sides <= 10:
    angle = 360 / shape_sides
    tim.color(random.random(),random.random(),random.random())
    for i in range(shape_sides):
        tim.forward(100)
        tim.right(angle)
    shape_sides +=1
    
screen = Screen()
screen.exitonclick()

    
    
















screen = Screen()
screen.exitonclick()


