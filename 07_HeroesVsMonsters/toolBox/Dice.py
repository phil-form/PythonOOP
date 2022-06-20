from random import randint


class Dice:
    def __init__(self, max) -> None:
        self.__min = 1
        self.__max = max

    @property
    def min(self):
        return self.__min

    @property
    def max(self):
        return self.__max

    def throw(self):
        return randint(self.min, self.max)
