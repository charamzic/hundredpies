print("""
.     /                 \---/
     / \                 |o|
     / \           _/"\_ | |
      |            |   | | |  _/"\_           \
         \       _/"\_  ===== |   |          / \
    \   / \      |   |   |o|_/"\_            / \
   / \  / \     _/"\_    | ||   |_/"\_    /   |      \
   / \   |      | _/"\_ /===\ _/"\_  |   / \        / \
    |             |   |       |   |      / \        / \
        \                                 |          |/
       / \   /    \           /      \        /      / \
       / \  / \  / \   /     / \    / \      / \     / \
        |   / \  / \  / \    / \    / \      / \      |
             |    |   / \     |      |        |
           \           |        \                  \
          / \    \       /     / \      /         / \
          / \   / \     / \    / \     / \        / \
           |    / \     / \     |      / \         |
                 |       |              |
                                                             ||---||
                                                             |__|__|
                                                              ``..``


-----------------------------------------------------------------------------------
You are in the middle of the woods. You can see a fire light blinking through the tree branches.
To your right, there is path through the woods, heading towards the light. On your left, you can 
hear something approaching.
""")

woods_dir = input("Where do you want to go, left, or right? ")
castle_dir = ""
princess_choice = ""


def for_less_fortunate():
    print("It's a complicated game and I'm tired pretending it's not.")


if woods_dir.lower() == "left":
    print("Are you mad? Just told you there is something in the dark!\nYou're dead.")
    exit()
elif woods_dir.lower() == "right":
    print("Yea yea, a little coward is with us, right? Alright, you are on the path.")
    print("After about one hour walk, you find yourself in front of the huge castle.")
    castle_dir = input(
        "You can climb the wall or knock on the door. What you choose? up / knock ")
else:
    for_less_fortunate()

if castle_dir.lower() == "up":
    print("\nYou climbed your way up to the princess chambers and she is staring at you terified.")
    princess_choice = input(
        "Will you - take her down with a karate chop [1], ask her what's the time [2] ")
elif castle_dir.lower() == "knock":
    print("\nNobody is answering, you felt asleep and a giant bunny killed you in a sleep.")
    exit()

if princess_choice.lower() == "1":
    print("\nAnd now you can do whatever you like. Just don't kiss her. She doesn't like it.")
    print("You won the game")
elif princess_choice.lower() == "2":
    print("\nIt's 'Get your ass out of here, intruder!' time. You've been arrested and sentenced to death.")
    print("Yes, you will die.")
else:
    for_less_fortunate()
