from Monster import Monster

class Goblin(Monster):

    def __init__(self):
        super().__init__()
        super().initiateRessources('gold')

    @property
    def force(self):
        return super().__force + 1