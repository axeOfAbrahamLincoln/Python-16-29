from turtle import Turtle

# Text alignment for scoreboard display
ALIGNMENT = "center"

# Font settings for score and high score text
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    """
    Displays and manages the player's score and high score.

    Inherits from Turtle to write text directly on the screen.
    """

    def __init__(self, shape="classic", undobuffersize=1000, visible=True):
        """Initialize the scoreboard and display the starting score."""
        super().__init__(shape, undobuffersize, visible)  # Initialize Turtle

        self.score = 0      # Current score
        with open("data.txt") as data:
            self.highscore = int(data.read())

        self.color("white")  # Text color
        self.penup()         # Prevent drawing lines
        self.goto(0, 260)    # Position scoreboard at top of screen

        self.hideturtle()    # Hide the turtle cursor
        self.display_score() # Show initial score

    def display_score(self):
        """Clear and redraw the current score and high score."""
        self.clear()  # Remove previous score text
        self.write(
            f"Score: {self.score} HighScore: {self.highscore}",
            align=ALIGNMENT,
            font=FONT
        )

    def reset(self):
        """
        Reset the score after a collision.

        Updates the high score if the player achieved
        a new record before resetting the score.
        """
        # Update high score if necessary
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
                

        self.score = 0       # Reset current score
        self.display_score() # Update scoreboard display

    def refresh(self):
        """Increase the score when food is eaten and update display."""
        self.score += 1      # Increase score
        self.display_score() # Redraw scoreboard