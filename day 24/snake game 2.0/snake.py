from turtle import Turtle

# Starting positions of the initial snake body segments
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# Distance the snake moves each step
MOVE_DISTANCE = 20

# Direction constants (degrees)
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    """
    Represents the snake in the Turtle-based Snake game.

    Handles creation of the snake, movement,
    body extension when food is eaten, and resetting
    after collisions.
    """

    def __init__(self):
        """Initialize the snake and create the starting body."""
        self.segments = []           # List storing all snake segments
        self.create_snake()          # Create the initial snake body
        self.head = self.segments[0] # Reference to the head segment

    def create_snake(self):
        """Create the initial snake using predefined positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)  # Add each starting segment

    def add_segment(self, position):
        """Create a new body segment at the given position."""
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()              # Prevent drawing lines
        new_segment.goto(position)       # Move to the specified position
        self.segments.append(new_segment)  # Add the segment to the snake list

    def extend_snake(self):
        """Add a new segment to the end of the snake."""
        # Place the new segment at the position of the current tail
        self.add_segment(self.segments[-1].pos())

    def reset(self):
        """
        Reset the snake after a collision.

        Existing segments are moved off-screen before the snake
        is recreated to avoid leaving old segments visible.
        """
        for seg in self.segments:
            seg.goto(1000, 1000)  # Move segments off-screen

        self.segments.clear()     # Remove old segment references
        self.create_snake()       # Recreate the starting snake
        self.head = self.segments[0]  # Reset head reference

    def move(self):
        """
        Move the snake forward.

        Each segment takes the position of the segment in front
        of it, then the head moves forward.
        """
        # Move body segments starting from the tail
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)  # Move the head forward

    def up(self):
        """Change direction to up unless the snake is moving down."""
        if self.head.heading() != DOWN:  # Prevent reversing into itself
            self.head.setheading(UP)

    def left(self):
        """Change direction to left unless the snake is moving right."""
        if self.head.heading() != RIGHT:  # Prevent reversing
            self.head.setheading(LEFT)

    def down(self):
        """Change direction to down unless the snake is moving up."""
        if self.head.heading() != UP:  # Prevent reversing
            self.head.setheading(DOWN)

    def right(self):
        """Change direction to right unless the snake is moving left."""
        if self.head.heading() != LEFT:  # Prevent reversing
            self.head.setheading(RIGHT)