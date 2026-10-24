from turtle import Turtle
import random

# Possible colors for the cars
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# Initial car movement speed
STARTING_MOVE_DISTANCE = 5

# Speed increase after each level
MOVE_INCREMENT = 5


class CarManager():
    """Manages creation, storage, and movement of cars in the game."""

    def __init__(self):
        """Initialize the car manager and set starting speed."""
        self.garage = []  # List storing all car objects
        self.make_car()   # Create the first car
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def make_car(self):
        """Randomly create a new car and add it to the garage."""
        random_chance = random.randint(1,6)

        # Only create a car if the random condition is met
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2)  # Stretch to look like a car
            new_car.penup()
            new_car.color(random.choice(COLORS))  # Random car color
            new_car.goto(300, random.randint(-250,250))  # Start at right side
            new_car.setheading(180)  # Face left
            self.garage.append(new_car)
        
    def car_starting(self):
        """Move all cars forward."""
        for car in self.garage:
            car.forward(self.car_speed)
    
    def car_speed_level_up(self):
        """Increase car speed when the player levels up."""
        self.car_speed += MOVE_INCREMENT