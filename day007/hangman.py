import os
import sys
import stages
from random_word import fetch_word


length = input(
    "Welcome to the hangman game.\nChoose length of the guessed word (max 12): ")
word = fetch_word(length)

if word is None:
    print("Sorry, something went wrong.")
    sys.exit()

placeholder = ""
for i in range(len(word)):
    placeholder += "_"


game_over = False
correct_letters = []
used_letters = []
mistakes = 0

while not game_over:
    guess = input("Guess a letter: ").lower()
    used_letters.append(guess)
    display = ""

    os.system('clear')

    for letter in word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in word:
        mistakes += 1
        print("\033[91mWrong guess.\033[0m")
        if mistakes == 6:
            game_over = True
            print("\033[91mYou lose!\033[0m")
            print(f"The correct word was: {word.upper()}")
    else:
        print("\033[92mCorrect guess, go on!\033[0m")

    print("\n" + display.upper())

    if "_" not in display:
        game_over = True
        print("You win!")

    print(stages.HANGMANPICS[mistakes])
    print(f"Used letters: {used_letters}\n")
