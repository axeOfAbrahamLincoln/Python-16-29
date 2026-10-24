from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.goto(100, 200)
        self.write(self.r_score, align="center", font = ("Courier", 80, "normal"))
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font = ("Courier", 80, "normal"))

    def l_score_increase(self):
        self.l_score += 1
    
    def r_score_increase(self):
        self.r_score += 1
    
    def game_over(self, player):
        self.update_scoreboard()
        self.home()
        self.write("Game Over", align="center", font=("Arial",25,"normal" ))
        self.goto(0,-50)
        self.write(f"winner {player}", align="center", font=("Arial",25,"normal"))