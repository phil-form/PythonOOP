from models.Monster.Monster import Monster
from interfaces.IGold import IGold

class Orc(Monster, IGold):
    def __init__(self) -> None:
        super().__init__()
        self.__gold = self.dice6.throw()

    @property
    def strength(self):
        return super().strength + 1

    def getGold(self):
        return self.__gold