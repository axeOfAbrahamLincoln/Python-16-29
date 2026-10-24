from turtle import Turtle

class Padle(Turtle):
    def __init__(self, position,name,shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.penup()
        self.goto(position)
        self.name = name
    
        self.label = Turtle()
        self.label.hideturtle()
        self.label.penup()
        self.label.color("white")
        self.label.setheading(90)
        self.update_label()
    
    def update_label(self):
        """Move label on top of paddle and redraw"""
        self.label.clear()
        self.label.goto(self.xcor(), self.ycor() + 50)
        self.label.write(self.name, align="center", font=("Courier", 14, "normal"))
        

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
