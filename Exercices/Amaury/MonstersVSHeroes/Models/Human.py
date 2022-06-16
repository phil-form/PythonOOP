from Hero import Hero

class Human(Hero):

    def __init__(self):
        super().__init__()

    @property
    def force(self):
        return super().force + 1

    @property
    def endurance(self):
        return super().endurance + 1
        