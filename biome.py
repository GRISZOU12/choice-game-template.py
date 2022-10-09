class Biome:

    def __init__(self):
        pass


class Plain(Biome):

    def __init__(self):
        super(Biome, self).__init__()

        self.floor_characteristic = {
            "Floor": "Dirt",
            "Relief": "Flat"
        }
