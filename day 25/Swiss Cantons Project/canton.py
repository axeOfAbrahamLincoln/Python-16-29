from turtle import Turtle, Screen
import time

screen = Screen()  # Create the main screen for drawing

# -----------------------------
# Canton class: handles writing and animating canton names
# -----------------------------
class Canton(Turtle):
    def __init__(self):
        super().__init__()           # Initialize Turtle
        self.hideturtle()            # Hide the turtle initially
        self.shape("circle")         # Shape of the turtle (used during animation)
        self.shapesize(stretch_len=0.3, stretch_wid=0.3)  # Make turtle small
        self.penup()                 # Avoid drawing lines while moving
        self.goto(300, 300)          # Start at upper-right corner

    # -----------------------------
    # Write canton abbreviation at specific coordinates
    # -----------------------------
    def write_canton(self, short, x, y):
        """Write a canton name at given coordinates."""
        self.goto(x, y)
        self.write(short, align="center", font=("Arial", 12, "normal"))

    # -----------------------------
    # Write end-of-game message at center
    # -----------------------------
    def write_game_end(self, message="Fantastic! You’re a true Swiss geography master!"):
        """Write the end game message at the center of the screen."""
        self.home()  # Go to center
        self.write(message, align="center", font=("Arial", 40, "normal"))

    # -----------------------------
    # Animate turtle flying to canton and write name
    # -----------------------------
    def fly_and_write(self, short, x, y, steps=15, delay=0.001):
        """
        Animate the turtle flying from current position to the canton coordinates
        and write the canton name.
        """
        self.showturtle()  # Make the turtle visible during animation

        # -----------------------------
        # Calculate incremental steps for smooth movement
        # -----------------------------
        # self.xcor() -> current x-coordinate of the turtle
        # self.ycor() -> current y-coordinate of the turtle
        # x, y       -> target coordinates where the canton should be written
        # steps      -> number of small movements to reach the target

        dx = (x - self.xcor()) / steps  # Amount to move in x-direction each step
        dy = (y - self.ycor()) / steps  # Amount to move in y-direction each step

        # Explanation:
        # 1. (x - self.xcor()) calculates the total distance horizontally.
        # 2. Dividing by 'steps' splits this distance into smaller increments for smooth animation.
        # 3. (y - self.ycor()) / steps does the same for vertical movement.
        # 4. During the loop below, the turtle moves by dx and dy each iteration,
        # reaching the target gradually instead of jumping instantly.

        # Move the turtle in small steps for animation effect
        for _ in range(steps):
            self.goto(self.xcor() + dx, self.ycor() + dy)
            screen.update()  # Update the drawing instantly
            time.sleep(delay)  # Small pause for smooth animation

        # Write the canton abbreviation at the target
        self.write_canton(short, x, y)
        self.hideturtle()  # Hide turtle after writing
        screen.update()    # Final update