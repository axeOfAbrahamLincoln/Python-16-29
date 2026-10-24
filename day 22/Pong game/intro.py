from turtle import Turtle, Screen

intro_text = (
    "🏓 PADDLE GAME\n\n"
    "Welcome to the Paddle Battle!\n\n"
    "Controls:\n\n"
    "Player 1 (Right Paddle)\n"
    "Up Arrow   - Move Up\n"
    "Down Arrow - Move Down\n\n"
    "Player 2 (Left Paddle)\n"
    "W - Move Up\n"
    "S - Move Down\n\n"
    "First player to reach 5 points wins!\n\n"
    "Press SPACE to start..."
)

class Intro(Turtle):
    def __init__(self, start_callback):
        super().__init__()
        self.screen = Screen()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,-180)
        self.write(intro_text, align="center", font=("Arial", 20, "bold"))

        self.screen.listen()
        self.screen.onkey(self.start_game, "space")

        self.start_callback = start_callback

    def start_game(self):
        self.clear()
        self.screen.onkey(None, "space")
        self.start_callback()