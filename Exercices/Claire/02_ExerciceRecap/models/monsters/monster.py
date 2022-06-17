from models.dice import Dice
from models.character import Character

class Monster(Character):

    def __init__(self, posX, posY, hasGold=False, hasLeather=False):
        super().__init__(posX, posY)
        self.gold = Dice(1, 6).throw() if hasGold else 0
        self.leather = Dice(1, 4).throw() if hasLeather else 0

    def __str__(self):
        return f": {self.currentHp}/{self.hp}"
        
    def loot(self):
        pass

    def shortName(self) -> str:
        pass
