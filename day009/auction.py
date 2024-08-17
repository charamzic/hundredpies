import os

# not using max() function for the dictionary to practice basics
# no input validation is in place

auction_details = {}


def find_winner(auction_details):
    highest_bid = 0
    highest_bidding_user = ""

    for user in auction_details:
        if auction_details[user] > highest_bid:
            highest_bid = auction_details[user]
            highest_bidding_user = user

    return f"""
          ============= AUCTION WINNER ================
        The highest bidding user is {highest_bidding_user} with a bid ${highest_bid}.
    """


should_continue = True

while should_continue:
    user = input("What is your name? ")
    user_bid = int(input("What is your bid? $"))

    auction_details[user] = user_bid

    next_user = input("Are there any more bidders? [y/n]: ")

    os.system('clear')

    if next_user == "n":
        should_continue = False
        print(find_winner(auction_details))
    elif next_user == "y":
        pass
    else:
        print("Wrong input.")
        break
