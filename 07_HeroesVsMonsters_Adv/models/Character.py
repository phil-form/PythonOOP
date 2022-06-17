from abc import ABC, abstractmethod
from toolBox.Dice import Dice
from toolBox.Generator import Generator
from models.Coordinate import Coordinate

class Character(ABC):
    def __init__(self, coor: Coordinate) -> None:
        self.__stamina = Generator.getStat()
        self.__strength = Generator.getStat()
        self.__health = self.maxHealth
        self.__dice4 = Dice(4)
        self.__dice6 = Dice(6)
        self.__coor = coor

    @property
    def stamina(self):
        return self.__stamina

    @property
    def strength(self):
        return self.__strength
    
    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property 
    def dice4(self):
        return self.__dice4

    @property 
    def dice6(self):
        return self.__dice6

    @property
    def coorX(self):
        return self.__coor.posX

    @coorX.setter
    def coorX(self, value):
        self.__coor.posX = value

    @property
    def coorY(self):
        return self.__coor.posY

    @coorY.setter
    def coorY(self, value):
        self.__coor.posY = value

    @property
    def maxHealth(self):
        return self.stamina + Generator.getModif(self.stamina)

    @property
    def race(self):
        return self.__class__.__name__

    def isDead(self):
        return self.health <= 0

    def hit(self, char):
        if not isinstance(char, Character):
            raise NameError("char MUST be of Character type.")

        damages = self.dice4.throw() + Generator.getModif(self.strength)

        char.__health -= damages

    @abstractmethod
    def getToken(self):
        pass

    def __eq__(self, __o: object) -> bool:
        if(isinstance(__o, Coordinate)):
            return self.__coor == __o
        return False

    def __str__(self) -> str:
        return f"str : {self.strength} stam : {self.stamina} health : {self.health} coord : {self.__coor}"