from random import randint

class Dice:

    def __init__(self, min, max):
        self.__min = min
        self.__max = max

    @property
    def min(self) -> int:
        return self.__min

    @property
    def max(self) -> int:
        return self.__max

    def throw(self) -> int:
        return randint(self.min, self.max)

    def manyThrow(self, total, keep):
        dices = [randint(self.min, self.max) for i in range (0, total)]
        return sum(sorted(dices, reverse=True)[:keep])
