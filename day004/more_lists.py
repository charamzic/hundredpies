import random


who_pays_the_bill = ["Peter", "Daniel", "Anna", "Gabriel", "Charlie"]
another_list = ["Karel", "Julie", "Robert", "Anežka"]
alltogether = [who_pays_the_bill, another_list]

print(who_pays_the_bill[random.randint(0, len(who_pays_the_bill) - 1)])

print(random.choice(who_pays_the_bill))

print(alltogether)
