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

    Handles creating the snake, moving it forward,
    extending its body, and controlling direction.
    """

    def __init__(self):
        """Initialize the snake and create the starting body."""
        self.segments = []
        self.create_snake()  # Create initial snake body
        self.head = self.segments[0]  # First segment is the head

    def create_snake(self):
        """Create the initial snake using predefined positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)  # Add each starting segment

    def add_segment(self, position):
        """Create a new body segment at the given position."""
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()  # Prevent drawing lines
        new_segment.goto(position)  # Move to given position
        self.segments.append(new_segment)  # Add to segment list

    def extend_snake(self):
        """Add a new segment to the end of the snake."""
        # Add new segment at the last segment's position
        self.add_segment(self.segments[-1].pos())

    def move(self):
        """
        Move the snake forward by shifting all segments.

        Each segment moves to the position of the segment
        in front of it, then the head moves forward.
        """
        # Move body segments from tail to head
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)  # Move head forward

    def up(self):
        """Change direction to up unless moving down."""
        if self.head.heading() != DOWN:  # Prevent reverse
            self.head.setheading(UP)

    def left(self):
        """Change direction to left unless moving right."""
        if self.head.heading() != RIGHT:  # Prevent reverse
            self.head.setheading(LEFT)

    def down(self):
        """Change direction to down unless moving up."""
        if self.head.heading() != UP:  # Prevent reverse
            self.head.setheading(DOWN)

    def right(self):
        """Change direction to right unless moving left."""
        if self.head.heading() != LEFT:  # Prevent reverse
            self.head.setheading(RIGHT)