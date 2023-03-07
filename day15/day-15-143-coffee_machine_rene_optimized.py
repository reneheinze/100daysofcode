MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# The profit I got :)
sum_money = 0


# This function got optimized
def check_money():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def show_report(my_money):
    """Takes the dictionary resources prints them on screen"""
    for value in resources:
        print(value.capitalize() + ": " + str(resources[value]))
    print("Money: " + str(my_money))


# This function got optimized
def check_ressources(user_choice, order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficant"""
    for item in order_ingredients:
        # If the order_ingredients at the key are greater then the resources
        # Key water with 200 in Menu is greater Key Water in ressources
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough water {item}.")
            return False
    return True


def substract_ressources(user_choice, order_ingredients):
    """Takes the dictionary resources and the variable user_choice. Then subtract the values from the chosen drink
    from the resources dictionary"""
    for item in order_ingredients:
        resources[user_choice] -= order_ingredients[item]



def main(my_money):
    """The main function that does the work"""
    user_choice = input("What would you like?(espresso/latte/cappuccino): ")
    # My input is report
    if user_choice == "report":
        show_report(my_money)

    # My input is a espresso / latte / cappuccino
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        order_ingredients = MENU[user_choice]["ingredients"]
        if check_ressources(user_choice, order_ingredients):
            money = check_money()
            costs = MENU[user_choice]['cost']
            if money > costs:
                print("Here is $" + str(round(money - costs, 2)) + " in change")
                print("Here is your " + user_choice + ". Enjoy!")
                substract_ressources(user_choice, MENU[user_choice]["ingredients"])
                my_money = my_money + MENU[user_choice]["cost"]

            else:
                print("Sorry that's not enough money. Money refunded.")

    # My input is off
    elif user_choice == "off":
        return

    main(my_money)


main(sum_money)
