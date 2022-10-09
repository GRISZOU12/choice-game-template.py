import functions
import player

players = player.Characters(100)
Lumberjack = player.Lumberjack()
Stonecutter = player.Stonecutter()

print("+--------------------\n|Welcome to THE GAME|\n+--------------------")

general_pause_reason = "|Press ENTER key to continue..."

while True:

    print(f"\n|To begin the adventure please choose one of those characters : \n1.{Lumberjack.Name}\n2.{Stonecutter.Name}\n")
    perso = input("|please enter the number of your choice [1|2] or 3 for characters description > ")

    try:

        perso = int(perso)

        if perso == Lumberjack.id:
            print(f"|Ok so your character will be the {Lumberjack.Name}")
            break

        elif perso == Stonecutter.id:
            print(f"|Ok so your character will be the {Stonecutter.Name}")
            break

        elif perso == 3:
            print(f" - {Lumberjack.Name} have the weapon : {Lumberjack.Weapon.__name__}")
            print(f" - {Stonecutter.Name} have the weapon : {Stonecutter.Weapon.__name__}")
            functions.pause(general_pause_reason)
            functions.clear()

        else:
            print(f"|Please enter 1 or 2 not : {perso}")
            functions.pause(general_pause_reason)
            functions.clear()

    except ValueError:

        print("|Please enter 1 or 2 not : (it's a string not an int)")

        functions.pause(general_pause_reason)
        functions.clear()
