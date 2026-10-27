import random
from turtle import Turtle


class Food(Turtle):
    """
    Represents the food object in the Snake game.

    The food appears at random positions on the screen.
    When the snake eats it, the food relocates to a new
    random position.
    """

    def __init__(self):
        """Initialize the food object and set its appearance."""
        super().__init__()  # Initialize Turtle parent class

        self.shape("circle")  # Set shape to circle
        self.color("red")  # Set food color
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)  # Make it smaller
        self.penup()  # Prevent drawing lines
        self.speed("fastest")  # Make movement instant

        self.refresh()  # Place food at random position

    def refresh(self):
        """Move the food to a new random position on the screen."""
        # Generate random coordinates within screen boundaries
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        self.goto(random_x, random_y)  # Move food to new location