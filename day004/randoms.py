import random
import my_module

print(random.randint(1, 22))
print(my_module.my_favourite_number)

while random.randint(0, 10) != 7:
    print(random.random() * 11 + 1)
    print(random.uniform(3, 6))

head_or_tail = random.randint(0, 1)

if head_or_tail == 1:
    print("Heads")
else:
    print("Tails")
