import random

class Dice():
    
    def __init__(self, max, min = 1):
        self.__max = max
        self.__min = min

    @property
    def min(self):
        return self.__min

    @property
    def max(self):
        return self.__max

    def roll(self):
        return random.randint(self.__min, self.__max)
