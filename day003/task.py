# if else conditions
age = int(input("How old are you, buddy? "))
have_money = input("Have money? y/n ")
# no validation done here


def is_wealthy():
    return have_money == 'y'


if 18 <= age < 80:  # age >= 18 and age < 80
    if is_wealthy():
        print("Here's your beer.")
    else:
        print("Get your ass outta here, beggar!")
elif age >= 80:
    if is_wealthy():
        print("Here's your beer and diaper, tiger.")
    else:
        print("It's on the house, veteran.")

    wanna_cab = input("Would you like me to call a cab for you later on? y/n ")
    if wanna_cab == 'y':
        print("Will be here at 9pm.")
    else:
        print("Alright then.")
else:
    print("Then just fok off, will ya?")

if age % 2 == 0:
    print("And your age is even, by the way.")
else:
    print("And your age is really odd, to be honest.")
