from models.Character import Character
from models.Monster.Monster import Monster
from interfaces.IGold import IGold
from interfaces.ILeather import ILeather

class Hero(Character, IGold, ILeather):
    def __init__(self, name) -> None:
        super().__init__()

        self.__name = name
        self.__gold = 0
        self.__leather = 0

    @property
    def name(self):
        return self.__name

    def getGold(self):
        return self.__gold

    def getLeather(self):
        return self.__leather

    def loot(self, monster: Monster):
        if isinstance(monster, IGold):
            self.__gold += monster.getGold()

        if isinstance(monster, ILeather):
            self.__leather += monster.getLeather()

    def rest(self):
        self.health = self.maxHealth

    def __str__(self) -> str:
        return f"{self.__name} str : {self.strength} stam : {self.stamina} health : {self.health}"
