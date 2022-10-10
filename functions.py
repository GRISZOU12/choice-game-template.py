"""
🖋️WRITTEN BY GRISZ
"""


import os

general_pause_reason = "|Press ENTER key to continue..."

def pause(reason):
    input(reason)
    # this function is here to pause the game


def clear():
    os.system("cls")
    # this function is here to clear the console


def two_choices(choice1, choice2, now_1, now_2, description):

    is_choice = True

    while is_choice:

        print(f"|Here you can : \n 1- {choice1}\n 2- {choice2}\n 3- show choices details")
        choice = input("\n| [1|2|3] > ")

        try:

            choice = int(choice)

            if choice == 1:
                print(now_1)
                is_choice = False
                break

            elif choice == 2:
                print(now_2)
                is_choice = False
                break

            elif choice == 3:
                print(description)
                pause(general_pause_reason)
                clear()

            else:
                print(f"|Please enter 1-2 or 3 not : {choice}")
                pause(general_pause_reason)
                clear()

        except ValueError:

            print("|Please enter 1 or 2 not : (it's a string not an int)")

            pause(general_pause_reason)
            clear()


"""
🖋️WRITTEN BY GRISZ
"""
