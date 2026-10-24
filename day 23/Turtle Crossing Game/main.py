import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Create the game screen
screen = Screen()
screen.setup(width=620, height=620)
screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0)  # Turn off automatic animation

# Create game objects
turtle_player = Player()
car = CarManager()
score = Scoreboard() 

# Listen for keyboard input
screen.listen()
screen.onkey(turtle_player.move, "Up")  # Move player when "Up" key is pressed

game_is_on = True

# Main game loop
while game_is_on:
    time.sleep(0.1)  # Control game speed
    screen.update()  # Manually update the screen

    # Create and move cars
    car.make_car()
    car.car_starting()
    
    # Check if player reached the finish line
    if turtle_player.is_at_finishline():
        turtle_player.go_to_start()   # Reset player position
        score.increase_score()        # Increase level
        car.car_speed_level_up()      # Increase car speed
    
    # Detect collision between player and cars
    for car_obj in car.garage:
        if abs(turtle_player.xcor() - car_obj.xcor()) < 20 and abs(turtle_player.ycor() - car_obj.ycor()) < 25:
            game_is_on = False
            score.game_over()  # Display game over message
            
# Close window when clicked
screen.exitonclick()