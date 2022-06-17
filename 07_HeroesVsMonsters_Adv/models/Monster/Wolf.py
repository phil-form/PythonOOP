from models.Monster.Monster import Monster
from interfaces.ILeather import ILeather

class Wolf(Monster, ILeather):
    def __init__(self, coor) -> None:
        super().__init__(coor)
        self.__leather = self.dice4.throw()

    def getLeather(self):
        return self.__leather

    def getToken(self):
        return ' W ' if not self.hidden else  ' * '