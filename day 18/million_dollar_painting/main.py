# Hirst-style dot painting using Turtle and colors extracted from an image
# Draws a 10x10 grid of colored dots with random colors from the source image



import colorgram
import turtle as t
import random

t.colormode(255)
colors = colorgram.extract("/Volumes/Macintosh HD Data/Coding/Python 2.0/day 18/million_dollar_painting/image.jpg",20)



def color_list(color_objects):
    """
    Converts a list of Colorgram color objects into a list of RGB tuples.

    Args:
        color_objects (list): A list of Colorgram color objects.

    Returns:
        list: A list of RGB tuples, each containing three integers (0-255).
    """
    rgb_list = []
    for item in color_objects:
        rgb_list.append(item.rgb)
    return rgb_list

def random_color(rgb_list):
    return random.choice(rgb_list)   

rgb_color_list = color_list(colors)
tim = t.Turtle()
tim.shape("turtle")
tim.speed(6)
tim.hideturtle()
start_x_coordinate = -220
start_y_coordinate = -200
tim.penup()


for vertical in range(10):
    tim.goto(start_x_coordinate , start_y_coordinate + vertical*50)
    for horizontal in range(10):
        tim.dot(20,random_color(rgb_color_list))
        tim.forward(50)



screen = t.Screen()
screen.exitonclick()