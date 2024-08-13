user_input = input("Feeling like being annoyed by pointles prints? [y/n]: ")
gibrish = """
No Hello World today!
Gonna need to look at my zsh setup, it behaves funny these days.
====================================================================
Let's see if ANSI works and \033[92mthis text is green.\033[0m Is it?
Why the \033[91mHELL!\033[0m is my terminal messes up longer lines of text?
Anyway, \033[94mcolouring works,\033[0m right?
"""

if user_input == 'y':
    print(gibrish)
elif user_input == 'n':
    print("meh... you could get " + str(len(gibrish)) +
          " amount of character, by the way")
else:
    print("Having little alphabetie problems, aren't we?")
