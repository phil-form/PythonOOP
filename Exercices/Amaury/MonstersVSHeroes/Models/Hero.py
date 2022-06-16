from Character import Character

class Hero(Character):

    def __init__(self):
        super().__init__()
        self.__stock = {'gold': 0, 'leather': 0}

    @property
    def stock(self):
        return self.__stock

    def strip(self, enemy):
        self.__stock['gold'] += enemy.gold
        self.__stock['leather'] += enemy.leather

    