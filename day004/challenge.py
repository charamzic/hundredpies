import random


game_list = ["rock", "paper", "scissors"]

user_input = input("What you choose? Rock [1], Paper [2], Scissors [3] ")
user_choice = game_list[int(user_input) - 1]
comp_choice = random.choice(game_list)


print(f"You have chosen: {user_choice}.")
print(f"The computer choice is: {comp_choice}.")


if user_choice == comp_choice:
    print("It's a draw.")
elif user_choice == "rock" and comp_choice == "scissors":
    print("You win!")
elif user_choice == "paper" and comp_choice == "rock":
    print("You win!")
elif user_choice == "scissors" and comp_choice == "paper":
    print("You win!")
else:
    print("Computer wins!")
