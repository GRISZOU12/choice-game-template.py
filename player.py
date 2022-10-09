import weapons
weapon = weapons.Weapons()
Axe = weapons.Axe
Hammer = weapons.Hammer


class Characters:

    def __init__(self, health):
        self.health = health


class Lumberjack(Characters):

    def __init__(self):
        super(Characters, self).__init__()
        self.id = 1
        self.Name = "Lumberjack"
        self.Weapon = Axe


class Stonecutter(Characters):

    def __init__(self):
        super(Characters, self).__init__()
        self.id = 2
        self.Name = "Stonecutter"
        self.Weapon = Hammer
