from turtle import Turtle

# Starting position of the player
STARTING_POSITION = (0, -280)

# Distance the player moves each step
MOVE_DISTANCE = 10

# Y-coordinate of the finish line
FINISH_LINE_Y = 280


class Player(Turtle):
    """Represents the player turtle and handles movement and position checks."""

    def __init__(self, shape="turtle", undobuffersize=1000, visible=True):
        """Initialize the player and place it at the starting position."""
        super().__init__(shape, undobuffersize, visible)
        self.setheading(90)  # Face upward
        self.penup()
        self.go_to_start()   # Move player to starting position
        
    def move(self):
        """Move the player upward by a fixed distance."""
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
    
    def go_to_start(self):
        """Return the player to the starting position."""
        self.goto(STARTING_POSITION)

    def is_at_finishline(self):
        """Check if the player has reached the finish line."""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False