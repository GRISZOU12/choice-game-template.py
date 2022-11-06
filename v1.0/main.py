"""
🖋️WRITTEN BY GRISZ
"""


import functions
import player
import biome
import random

launch = True
players = player.Characters(100)
Lumberjack = player.Lumberjack()
Stonecutter = player.Stonecutter()

biomes = biome.Biome()
biome_plain = biome.Plain()
biome_desert = biome.Desert()

functions.clear()
print("+--------------------\n|Welcome to THE GAME|\n+--------------------")


while launch:

    print(f"\n|To begin the adventure please choose one of those characters : \n1.{Lumberjack.Name}\n2.{Stonecutter.Name}\n")
    perso = input("|please enter the number of your choice [1|2] or 3 for characters description > ")

    try:

        perso = int(perso)

        if perso == Lumberjack.Id:
            print(f"|Ok so your character will be the {Lumberjack.Name}")
            launch = False
            break

        elif perso == Stonecutter.Id:
            print(f"|Ok so your character will be the {Stonecutter.Name}")
            launch = False
            break

        elif perso == 3:
            print(f" - {Lumberjack.Name} have the weapon : {Lumberjack.Weapon.__name__}")
            print(f" - {Stonecutter.Name} have the weapon : {Stonecutter.Weapon.__name__}")
            functions.pause(functions.general_pause_reason)
            functions.clear()

        else:
            print(f"|Please enter 1 or 2 not : {perso}")
            functions.pause(functions.general_pause_reason)
            functions.clear()

    except ValueError:

        print("|Please enter 1 or 2 not : (it's a string not an int)")

        functions.pause(functions.general_pause_reason)
        functions.clear()


random_biome_Id = random.randint(1, 2)

if random_biome_Id == biome_plain.Id:
    spawn_biome = biome_plain.Name
elif random_biome_Id == biome_desert.Id:
    spawn_biome = biome_desert.Name

print(f"|You spawned in : {spawn_biome}\n")

functions.two_choices("Go to the north", "Go to the south", "|You are in front of a river", "|You are in front of a mountain", "|In north there is a river but in south there is a village")


"""
🖋️WRITTEN BY GRISZ
"""
