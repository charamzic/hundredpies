import os
import random
from art import black_jack_title


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        # ace can be both, 11 or 1 if over 21
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(usr_score, cp_score):
    if usr_score == cp_score:
        return "Draw!"
    elif cp_score == 0:
        return "\033[91mYou loose. Opponent has Blackjack!\033[0m"
    elif usr_score == 0:
        return "\033[92mWin with a Blackjack!\033[0m"
    elif usr_score > 21:
        return "\033[91mYou loose. You went over 21.\033[0m"
    elif cp_score > 21:
        return "\033[92mOpponent went over 21. You win!\033[0m"
    elif usr_score > cp_score:
        return "\033[92mYou win!\033[0m"
    else:
        return "\033[91mYou loose!\033[0m"


def play_game():
    user_cards = []
    comp_cards = []
    is_game_over = False
    user_score = -1
    comp_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"Your cards {user_cards} and current score {user_score}.")
        print(f"Computer's first card: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(f"\n=====\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))


while input("\nDo you want to play a game of Blackjack? [y/n]: ") == 'y':
    os.system("clear")
    print(black_jack_title)
    play_game()
