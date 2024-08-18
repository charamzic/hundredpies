import os
from random import randint

EASY = 10
HARD = 5

number_to_guess = randint(1, 50)


def set_rounds(chosen_level):
    if chosen_level == 'e':
        return EASY
    elif chosen_level == 'h':
        return HARD


def play():
    level = input(
        "Type 'e' for easy difficulty or 'h' for hard difficulty: ")
    rounds = 0

    if level == 'e':
        rounds = EASY
        print(f"Chosen difficulty: EASY. You have {EASY} guesses.")
    elif level == 'h':
        rounds = HARD
        print(f"Chosen difficulty: HARD. You have {HARD} guesses.")
    else:
        print(f"Wrong input: {level}")
        play()

    while rounds > 0:
        guessed = int(input("Guess the number between 1 and 50: "))

        if guessed > number_to_guess:
            print("Too high.")
        elif guessed < number_to_guess:
            print("Too low")
        else:
            print(f"\n=== You got it! The right number is {
                  number_to_guess}. ===")
            rounds = 0

        rounds -= 1
        if rounds == 0:
            print(f"You are out of guesses. The right number was {
                  number_to_guess}.")


while input("\nWanna play Guess The Number game? [y/n]: ") == 'y':
    os.system("clear")
    play()
