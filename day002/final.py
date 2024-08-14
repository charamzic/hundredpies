total_amount = float(input("What is the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? %"))
persons = int(input("How many people to split the bill? "))
print(f"Each person should pay ${
      (total_amount * (tip / 100) + total_amount) / 2}")
