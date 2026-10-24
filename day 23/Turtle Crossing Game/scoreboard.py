from turtle import Turtle

# Font used for all scoreboard text
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Handles the display of the game level and game over message."""

    def __init__(self, shape="classic", undobuffersize=1000, visible=False):
        """Initialize the scoreboard and display the starting level."""
        super().__init__(shape, undobuffersize, visible)
        self.level = 1  # Starting level
        self.penup()
        self.goto(-180, 260)  # Position of the level display
        self.write(f"L E V E L:{self.level}", align="center", font=FONT)
        
    def increase_score(self):
        """Increase the level and update the display."""
        self.level += 1
        self.clear()  # Remove previous text
        self.write(f"L E V E L:{self.level}", align="center", font=FONT)
    
    def game_over(self):
        """Display the 'Game Over' message in the center of the screen."""
        self.home()  # Move turtle to the center
        self.write("G A M E   O V E R", align="center", font=FONT)