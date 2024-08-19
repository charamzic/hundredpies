from machine import MENU, resources, send_report


def get_recources():
    for item in resources:
        print(f"{item}: {resources[item]}")


def get_product(product):
    if product in MENU:
        print(MENU[product])
        print(MENU[product]["ingredients"])


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Calculates the total and returns it as float"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


profit = 0


def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted.
       Returns False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappucino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(send_report())
        print(f"Earnings: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
