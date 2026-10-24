import turtle as t
import random

t.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
start_y_positions = [-100, -50, 0, 50, 100, 150]
def makes_finishline():
    finish_line = t.Turtle()
    finish_line.penup()
    finish_line.goto(x=230,y=-150)
    finish_line.pendown()
    finish_line.goto(x=230,y=200)



for turtle_index in range (0,6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=start_y_positions[turtle_index])
    all_turtles.append(new_turtle)


is_race_on = False
user_bet = t.textinput(title="Make your bet", prompt=f"Which turtle will win the race? \n {colors} \nEnter a color: ")

if user_bet:
    is_race_on = True
    makes_finishline()
    
while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                t.write(f"You have won.\nThe {winning_color} turtle won the race", align="center", font=("Arial", 24, "bold"))
                
            else:
                t.write(f"You have lost.\nThe {winning_color} turtle won the race", align="center", font=("Arial", 24, "bold"))
        turtle.forward(random.randint(0,10))
        



t.exitonclick()