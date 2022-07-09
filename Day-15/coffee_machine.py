from coffee_menu import menu, resources, profit


# TODO: 4. Check resources sufficient?
def is_resources_sufficient(order_ingredients):
    """Returns True when order can be made and False if ingredients is insufficient."""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return is_enough


# TODO: 5. Process coins.
def process_coins():
    """Returns calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters? ")) * 0.25
    total += int(input("how many dimes? ")) * 0.1
    total += int(input("how many nickles? ")) * 0.05
    total += int(input("how many pennies? ")) * 0.01
    return total


# TODO: 6. Check transaction successful?
def is_transaction_successful(money_recieved, drink_cost):
    """Return True when payment is accepted, or False when payment is insufficient"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money. Money refunded.")
        return False


# TODO: 7. Make Coffee.
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


is_on = True

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == "off":
        is_on = False
    # TODO: 3. Print report.
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = menu[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])