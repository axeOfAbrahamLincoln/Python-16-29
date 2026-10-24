from turtle import Turtle

# Text alignment for scoreboard display
ALIGNMENT = "center"

# Font settings for score and game over text
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    """
    Displays and manages the game score.

    Inherits from Turtle to write text on the screen.
    Handles score updates and displays the game over message.
    """

    def __init__(self, shape="classic", undobuffersize=1000, visible=True):
        """Initialize the scoreboard and display the starting score."""
        super().__init__(shape, undobuffersize, visible)  # Initialize Turtle

        self.score = 0  # Starting score
        self.color("white")  # Text color
        self.penup()  # Prevent drawing lines
        self.goto(0, 260)  # Move to top of screen
        self.display_score()
        self.hideturtle()  # Hide turtle cursor

    def display_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)  # Display score


    def game_over(self):
        """Display the 'GAME OVER' message at the center of the screen."""
        self.goto(0, 0)  # Move to center
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def refresh(self):
        """Update the score display after the snake eats food."""
        self.clear()  # Remove previous score
        self.score += 1  # Increase score
        self.display_score()