print("Welcome tho Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M, or L? ")
pepperoni = input("Do you want pepperoni on your pizza? y/n ")
extra_cheese = input("Do you want an extra cheese? y/n ")
total_bill = 0

if size == 'S':
    total_bill += 15
    if pepperoni == 'y':
        total_bill += 2
elif size == 'M':
    total_bill += 20
    if pepperoni == 'y':
        total_bill += 3
else:
    total_bill += 25
    if pepperoni == 'y':
        total_bill += 3

if extra_cheese == 'y':
    total_bill += 1

print(f"It will be ${total_bill}, please.")

# logical operators and, or, not
