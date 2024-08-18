try:
    age = int(input("How old are you? "))
except ValueError:
    print("You have inputed an invalid number. Age must be numerical.")
    age = int(input("How old are you? "))
