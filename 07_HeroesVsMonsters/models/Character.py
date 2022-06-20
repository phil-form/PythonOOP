from toolBox.Dice import Dice
from toolBox.Generator import Generator

class Character:
    def __init__(self) -> None:
        self.__stamina = Generator.getStat()
        self.__strength = Generator.getStat()
        self.__health = self.maxHealth
        self.__dice4 = Dice(4)
        self.__dice6 = Dice(6)

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