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

coins = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0
}

# The profit I got :)
sum_money = 0


def check_money(input_coins):
    """Takes the dictionary coins, inputs the money types from the user and returns the calculated sum."""
    print("Please insert coins.")
    input_coins["quarters"] = int(input("how many quarters?: "))
    input_coins["dimes"] = int(input("how many dimes?: "))
    input_coins["nickles"] = int(input("how many nickels?: "))
    input_coins["pennies"] = int(input("how many pennies?: "))
    input_money = input_coins["quarters"] * 0.25 + input_coins["dimes"] * 0.1 + input_coins["nickles"] * 0.05 + \
                  input_coins["pennies"] * 0.01
    return input_money


def show_report(resources, my_money):
    """Takes the dictionary resources prints them on screen"""
    for value in resources:
        print(value.capitalize() + ": " + str(resources[value]))
    print("Money: " + str(my_money))


def check_ressources(local_resources, user_choice):
    """Takes the dictionary resources and variable user_choice and checks if there are enough resources.
    Returns True or False """
    if (local_resources["water"] - MENU[user_choice]["ingredients"]["water"]) < 0:
        print("Sorry there is not enough water.")
        return False
    if (local_resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"]) < 0:
        print("Sorry there is not enough coffee.")
        return False
    if user_choice == "espresso":
        return True
    if (local_resources["milk"] - MENU[user_choice]["ingredients"]["milk"]) < 0:
        print("Sorry there is not enough milk.")
        return False
    return True


def substract_ressources(local_resources, user_choice):
    """Takes the dictionary resources and the variable user_choice. Then subtract the values from the chosen drink
    from the resources dictionary"""
    local_resources["water"] = local_resources["water"] - MENU[user_choice]["ingredients"]["water"]
    local_resources["coffee"] = local_resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"]
    if user_choice == "espresso":
        return
    local_resources["milk"] = local_resources["milk"] - MENU[user_choice]["ingredients"]["milk"]
    return


def main(local_resources, my_money):
    """The main function that does the work"""
    user_choice = input("What would you like?(espresso/latte/cappuccino): ")
    # My input is report
    if user_choice == "report":
        show_report(local_resources,my_money)

    # My input is a espresso / latte / cappuccino
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        if check_ressources(local_resources, user_choice):
            money = check_money(coins)
            costs = MENU[user_choice]['cost']
            if money > MENU[user_choice]['cost']:
                print("Here is $" + str(round(money - costs, 2)) + " in change")
                print("Here is your " + user_choice + ". Enjoy!")
                substract_ressources(local_resources, user_choice)
                my_money = my_money + MENU[user_choice]["cost"]

            else:
                print("Sorry that's not enough money. Money refunded.")

    # My input is off
    elif user_choice == "off":
        return

    main(local_resources, my_money)


main(resources, sum_money)
