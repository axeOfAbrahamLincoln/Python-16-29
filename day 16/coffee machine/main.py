from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
menu = Menu()
money = MoneyMachine()


is_machine_on = True

while is_machine_on:
    user_choice = input(f"What would you like? {menu.get_items()}:").lower()

    if user_choice == "off":
        is_machine_on = False
    elif user_choice == "report":
        coffee.report()
    else:
        user_drink = menu.find_drink(user_choice)
        if coffee.is_resource_sufficient(user_drink):
            if money.make_payment(user_drink.cost):
                coffee.make_coffee(user_drink)
