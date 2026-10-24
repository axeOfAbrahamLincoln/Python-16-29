import turtle as t

tim = t.Turtle()
tim.shape("turtle")

def forward():
    tim.forward(5)
def backward():
    tim.backward(5)
def left():
    tim.left(5)
def right():
    tim.right(5)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

t.listen()

t.onkey(fun=forward, key="w")
t.onkey(fun=backward, key="s")
t.onkey(fun=left, key="a")
t.onkey(fun=right, key="d")
t.onkey(fun=clear, key="c")


t.exitonclick()