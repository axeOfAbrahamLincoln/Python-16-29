# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.fd(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

my_table = PrettyTable()

my_table.add_column("Car Types",["Ferrari", "Audi", "BMW", "Toyota"])
my_table.add_column("Car Colors",["Red", "Black", "White", "Grey"])
my_table.align = "l"


print(my_table)
