from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_running = True

# Create instances as needed
# I name the object completely the same but in lower case
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while is_running:
    print(f"What would you like? ({menu.get_items()}):")
    user_choice = input()
    if user_choice == "off":
        is_running = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # create menuitem from chosen drink
        drink = menu.find_drink(user_choice)
        # Checks if there are enough resources by using the menuitem object
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # Makes the payment
            if :
                # Makes coffee
                coffee_maker.make_coffee(drink)