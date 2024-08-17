import os
from operations_file import add, subtract, multiply, divide


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    should_accumulate = True
    num1 = float(input("What is your first number? "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        op_symb = input("Pick an operation: ")
        num2 = float(input("What is the next number? "))
        result = operations[op_symb](num1, num2)
        print(f"{num1} {op_symb} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {
                       result}, or 'n' to start fresh: ")

        if choice == "y":
            num1 = result
        else:
            should_accumulate = False
            os.system("clear")
            calculator()


calculator()
