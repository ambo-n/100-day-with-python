from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
coin_processor = MoneyMachine()
while True:
    options = menu.get_items()
    user_input = input(f"What would you like? {options}: ").lower()
    if user_input == 'report':
        coffee_machine.report()
        coin_processor.report()
    elif user_input in menu.get_items():
        drink = menu.find_drink(user_input)
        if coffee_machine.is_resource_sufficient(drink) and coin_processor.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
    elif user_input == 'off':
        break
    else:
        print("Invalid input. Please try again")


