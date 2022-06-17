from models.Character import Character
from models.Monster.Monster import Monster
from interfaces.IGold import IGold
from interfaces.ILeather import ILeather
from enums.Direction import Direction
from toolBox.Generator import Generator

class Hero(Character, IGold, ILeather):
    def __init__(self, name, coor) -> None:
        super().__init__(coor)

        self.__name = name
        self.__gold = 0
        self.__leather = 0
        self.__killCount = 0

    @property
    def name(self):
        return self.__name

    @property
    def killCount(self):
        return self.__killCount
    
    @killCount.setter
    def killCount(self, value):
        self.__killCount = value

    @property
    def maxHealth(self):
        return self.stamina + Generator.getModif(self.stamina) + 2000

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


    def move(self, direction: Direction):
        if direction == Direction.NORTH:
            self.coorX -= 1
        elif direction == Direction.SOUTH:
            self.coorX += 1
        elif direction == Direction.EAST:
            self.coorY += 1
        else:
            self.coorY -= 1
            

    def __str__(self) -> str:
        return f"{self.__name} " + super().__str__()

    def getToken(self):
        return ' H ' if not self.isDead() else ' X '