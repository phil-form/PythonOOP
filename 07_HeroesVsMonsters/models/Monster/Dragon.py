from models.Monster.Monster import Monster
from interfaces.IGold import IGold
from interfaces.ILeather import ILeather

class Dragon(Monster, IGold, ILeather):
    def __init__(self) -> None:
        super().__init__()
        self.__leather = self.dice4.throw()
        self.__gold = self.dice6.throw()

    @property
    def stamina(self):
        return super().stamina + 1

    def getGold(self):
        return self.__gold

    def getLeather(self):
        return self.__leather