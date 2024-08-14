import random


heroes = [
    "Hercules", "Achilles", "Theseus",
    "Odysseus", "Perseus", "Bellerophon", "Jason"
]

longest_name = ""

for hero in heroes:
    if len(hero) > len(longest_name):
        longest_name = hero
    print(hero)
print("The longest name: " + longest_name)

shortest_name = longest_name

for num in range(0, len(heroes)):
    if len(heroes[num]) < len(shortest_name):
        shortest_name = heroes[num]
print("The shortest name: " + shortest_name)


print("===========\nWelcome to the one and only tricky hacky password generator!")
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like in your password? "))
nr_numbers = int(input("How many numbers would you like in your password? "))

pwd_list = []

for i in range(0, nr_letters):
    char = chr(random.randint(65, 90))
    if i % 2 == 0:
        char = char.lower()
    pwd_list.append(char)


for i in range(0, nr_symbols):
    pwd_list.append(chr(random.randint(33, 38)))


for i in range(0, nr_numbers):
    pwd_list.append(str(random.randint(1, 9)))


random.shuffle(pwd_list)
print("".join(pwd_list))
