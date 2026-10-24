import turtle
import pandas as pd
from canton import Canton

# -----------------------------
# Set up the game screen
# -----------------------------
screen = turtle.Screen()
screen.title("Swiss Canton Game")  # Window title
image = "suisse68.gif"             # Image of Switzerland map
screen.addshape(image)              # Add image as a turtle shape
screen.setup(width=1040, height=697)  # Set window size
turtle.shape(image)                 # Use the map image as the turtle shape

# -----------------------------
# Load canton data
# -----------------------------
# CSV should contain: canton name, short code, x/y coordinates
data = pd.read_csv("swiss_canton_coordinates.csv")
guessed = []  # Keep track of correctly guessed cantons

# -----------------------------
# Initialize Canton handler
# -----------------------------
canton = Canton()  # Custom class to draw/write on the map
screen.tracer(0)   # Turn off automatic screen updates for smoother drawing

# -----------------------------
# Main game loop
# -----------------------------
game_on = True
while game_on:
    # Ask the player to guess a canton
    answer_canton = screen.textinput(
        title=f"{len(guessed)}/26 Cantons Correct",
        prompt="Guess another canton:"
    ).title()  # Capitalize first letter of each word

    # -----------------------------
    # Check the guess
    # -----------------------------
    # Loop through each row of the CSV as a named tuple
    # .itertuples() allows access via row.column_name
    for row in data.itertuples():
        # row.cantons -> full canton name
        # row.short   -> short code for the canton (to display on map)
        # row.x, row.y -> coordinates to place the text on the map
        if row.cantons == answer_canton and row.shorts not in guessed:
            canton.fly_and_write(row.shorts, row.x, row.y)  # Draw abbreviation on map
            guessed.append(row.shorts)  # Add to guessed list

    # End the game when all 26 cantons are guessed
    if len(guessed) == 26:
        game_on = False

# -----------------------------
# Game end
# -----------------------------
canton.write_game_end()  # Display final message or results

# Close the screen on click
screen.exitonclick()