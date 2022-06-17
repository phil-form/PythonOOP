from models.dice import Dice
from abc import ABC

class Character(ABC): 

    def __init__(self, posX, posY):
        dice = Dice(1, 6)
        self.__stamina = dice.manyThrow(4, 3)
        self.__strength = dice.manyThrow(4, 3)
        self.__hp = self.__getHP()
        self.__currentHp = self.__hp
        self.__leather = 0
        self.__gold = 0
        self.__posX = posX
        self.__posY = posY

    def __long_str__(self):
        return f"{self.strength} str ; {self.stamina} stam ; {self.currentHp}/{self.hp} hp ; {self.gold} golds ; {self.leather} leathers"

    # begin region properties

    @property
    def stamina(self) -> int:
        return self.__stamina
    
    @property
    def strength(self) -> int:
        return self.__strength

    @property
    def hp(self) -> int:
        return self.__hp

    @property
    def currentHp(self) -> int:
        return self.__currentHp

    @currentHp.setter
    def currentHp(self, value: int):
        self.__currentHp = value

    @property
    def gold(self):
        return self.__gold

    @gold.setter
    def gold(self, value: int):
        self.__gold = value

    @property
    def leather(self):
        return self.__leather

    @leather.setter
    def leather(self, value: int):
        self.__leather = value

    @property
    def posX(self):
        return self.__posX

    @posX.setter
    def posX(self, value: int):
        self.__posX = value

    @property
    def posY(self):
        return self.__posY

    @posY.setter
    def posY(self, value: int):
        self.__posY = value

    # end region

    # begin region methods
    def isDead(self) -> bool:
        return self.currentHp <= 0

    def doAttack(self, target):
        damage = Dice(1, 4).throw() + self.__modifier(self.strength)
        target.getAttacked(damage)
        #print(f"> {self} dealt {damage} damage to {target} !")
        if target.isDead():
            print(f"{self} defeated {target}")

    def getAttacked(self, damage: int):
        self.__currentHp = self.currentHp - damage 
            
    def __getHP(self) -> int:
        return self.stamina + self.__modifier(self.stamina)

    def __modifier(self, base):
        if base < 5:
            return 1
        elif base < 10:
            return 0
        elif base < 15:
            return 1
        else:
            return 2
    # end region
