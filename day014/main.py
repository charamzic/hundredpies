import os
import random
from data import IG_ACCOUNTS


def check_answer(user_guess, a_foll, b_foll):
    if a_foll > b_foll:
        return user_guess == 'a'
    else:
        return user_guess == 'b'


score = 0
game_continues = True
acc_a = random.choice(IG_ACCOUNTS)

while game_continues:
    acc_b = random.choice(IG_ACCOUNTS)
    if acc_a == acc_b:
        acc_b = random.choice(IG_ACCOUNTS)

    print(f"Compare A: {acc_a["name"]}.")
    print("\n=== VERSUS ===\n")
    print(f"Against B: {acc_b["name"]}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    os.system("clear")

    is_correct = check_answer(guess, acc_a["followers"], acc_b["followers"])

    if is_correct:
        score += 1
        acc_a = acc_b
        print(f"You're right! Current score: {score}\n")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_continues = False
