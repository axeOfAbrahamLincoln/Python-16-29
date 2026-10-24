from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# ---------------------- SCREEN SETUP ----------------------

screen = Screen()
screen.setup(width=600, height=600)  # Set window size
screen.bgcolor("black")  # Set background color
screen.title("Snake Game")  # Set window title
screen.tracer(0)  # Turn off automatic screen updates (manual control)


# ---------------------- GAME OBJECTS ----------------------

snake = Snake()  # Create snake object
food = Food()  # Create food object
scoreboard = Scoreboard()  # Create scoreboard object


# ---------------------- KEYBOARD CONTROLS ----------------------

screen.listen()  # Listen for key presses
screen.onkey(snake.up, "Up")  # Move snake up
screen.onkey(snake.down, "Down")  # Move snake down
screen.onkey(snake.left, "Left")  # Move snake left
screen.onkey(snake.right, "Right")  # Move snake right


# ---------------------- GAME LOOP ----------------------

game_on = True  # Control variable for main loop

while game_on:
    screen.update()  # Manually refresh screen
    time.sleep(0.1)  # Control game speed

    snake.move()  # Move snake forward

    # -------- Detect collision with food --------
    if snake.head.distance(food) < 15:
        snake.extend_snake()  # Add new body segment
        food.refresh()  # Move food to new random position
        scoreboard.refresh()  # Increase score

    # -------- Detect collision with wall --------
    # If snake crosses screen boundary, end game
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_on = False
        scoreboard.game_over()

    # -------- Detect collision with tail --------
    # Skip the head and check remaining segments
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()


# ---------------------- EXIT ON CLICK ----------------------

screen.exitonclick()  # Close window when clicked