import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

# ---------------------- SCREEN SETUP ----------------------
# Configure the game window and disable automatic screen updates.

screen = Screen()
screen.setup(width=610, height=610)  # Set window size
screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor("black")              # Set background color
screen.title("Snake Game")           # Window title
screen.tracer(0)                     # Disable automatic animation updates


# ---------------------- GAME OBJECTS ----------------------
# Create the main game components.

snake = Snake()          # Player-controlled snake
food = Food()            # Food object that the snake eats
scoreboard = Scoreboard()  # Score and high score display


# ---------------------- KEYBOARD CONTROLS ----------------------
# Bind arrow keys to snake movement methods.

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# ---------------------- GAME LOOP ----------------------
# Main loop that continuously updates the game state.

game_on = True

while game_on:
    screen.update()       # Manually refresh the screen
    time.sleep(0.1)       # Control game speed

    snake.move()          # Move the snake forward

    # -------- Detect collision with food --------
    if snake.head.distance(food) < 15:
        snake.extend_snake()  # Grow the snake
        food.refresh()        # Move food to a new random position
        scoreboard.refresh()  # Increase score

    # -------- Detect collision with wall --------
    # Reset the game if the snake leaves the screen boundaries.
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        scoreboard.reset()
        snake.reset()

    # -------- Detect collision with tail --------
    # If the head touches any body segment, reset the game.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


# ---------------------- EXIT ON CLICK ----------------------
# Keep the window open until the user clicks it.

screen.exitonclick()