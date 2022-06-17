from models.character import Character
from models.monsters.monster import Monster
class Hero(Character):

    def __init__(self, name, posX, posY):
        super().__init__(posX, posY)
        self.__name = name

    @property
    def name(self):
        return self.__name

    def resetHp(self):
        self.currentHp = self.hp
        
    def loot(self, target: Monster):
        loots = target.loot()
        self.gold += loots["gold"] if "gold" in loots else 0
        self.leather += loots["leather"] if "leather" in loots else 0