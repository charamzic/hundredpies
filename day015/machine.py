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
    "cappucino": {
        "ingredients": {
            "water": 150,
            "milk": 80,
            "coffee": 18,
        },
        "cost": 2.3,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def send_report():
    return f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g"
