from Monster import Monster

class Dragon(Monster):

    def __init__(self):
        super().__init__()
        super().initiateRessources('gold')
        super().initiateRessources('leather')

    @property
    def endurance(self):
        return super().__endurance + 1
