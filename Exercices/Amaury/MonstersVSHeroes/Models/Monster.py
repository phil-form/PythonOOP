from Character import Character
from Dice import Dice

class Monster(Character):

    def __init__(self):
        super().__init__()
        self.__gold = 0
        self.__leather = 0

    @property
    def gold(self):
        return self.__gold

    @property
    def leather(self):
        return self.__leather
    
    def __createGold(self):
        dice = Dice(6)
        return dice.roll()

    def __createLeather(self):
        dice = Dice(4)
        return dice.roll()

    def initiateRessources(self, type):
        if (type == 'gold'):
            self.__gold = self.__createGold()
        if (type == 'leather'):
            self.__leather = self.__createLeather()