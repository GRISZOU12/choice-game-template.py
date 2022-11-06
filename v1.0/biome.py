"""
🖋️WRITTEN BY GRISZ
"""


class Biome:

    def __init__(self):
        pass


class Plain(Biome):

    def __init__(self):
        super(Biome, self).__init__()

        self.Id = 1
        self.Name = "Plain"

        self.floor_characteristic = {
            "Floor": "Dirt",
            "Relief": "Flat"
        }


class Desert(Biome):

    def __init__(self):
        super(Biome, self).__init__()

        self.Id = 2
        self.Name = "Desert"

        self.floor_characteristic = {
            "Floor": "Sand",
            "Relief": "Dune"
        }

        
"""
🖋️WRITTEN BY GRISZ
"""
