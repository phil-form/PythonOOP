from models.Monster.Monster import Monster
from interfaces.ILeather import ILeather

class Wolf(Monster, ILeather):
    def __init__(self) -> None:
        super().__init__()
        self.__leather = self.dice4.throw()

    def getLeather(self):
        return self.__leather