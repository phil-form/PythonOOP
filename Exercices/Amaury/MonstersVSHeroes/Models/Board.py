import random
from Human import Human
from Dwarf import Dwarf
from Wolf import Wolf
from Dragon import Dragon
from Goblin import Goblin

class Board():

    def __init__(self):
        self.__cases = [[] for i in range(15)]
        self.__initiateForest()

    @property
    def cases(self):
        return self.__cases


    def __initiateForest(self):
        for i in range(15):
            for j in range(15):
                self.__cases[i].append(' . ')

    def __generateMonster(self):
        rand = random.randint(0, 2)
        if rand == 0:
            return Wolf()
        elif rand == 1:
            return Dragon()
        else:
            return Goblin()

    def addMonsters(self, number):
        n = number
        while n > 0:
            i = random.randint(0, 14)
            j = random.randint(0, 14)

            if ((i == 0 and j == 0) 
            or (i == 1 and j == 0) 
            or (i == 0 and j == 1) 
            or (i == 1 and j == 1)):
                self.addMonsters(n)

            else:
                if self.__cases[i][j] == ' . ':
                    check = False
                    for up in range(max(0, j - 1), max(0, j - 3), -1):
                        if self.__cases[i][j] and self.__cases[i][j] == ' . ':
                            check = True
                    for down in range(min(14, j + 1), min(14, j + 3), 1):
                        if self.__cases[i][j] and self.__cases[i][j] == ' . ':
                            check = True
                    for right in range(min(14, i + 1), min(14, i + 3), 1):
                        if self.__cases[i][j] and self.__cases[i][j] == ' . ':
                            check = True
                    for left in range(max(0, i - 1), max(0, i - 3), -1):
                        if self.__cases[i][j] and self.__cases[i][j] == ' . ':
                            check = True

                    if check == False:
                        self.__cases[i][j] = self.__generateMonster()
                        n -= 1
                    else: 
                        self.addMonsters(n)
                else:
                    self.addMonsters(n)

    def setHeroOnMap(self, hero):
        for i in range(15):
            for j in range(15):
                if self.__cases[i][j] == hero:
                    self.__cases[i][j] = ' . '

        if self.__cases[hero.x + 1, hero.y]:
            self.__cases[hero.x][hero.y] = hero

            if self.__cases[hero.x + 1, hero.y] != ' . ':
                return [self.__cases[hero.x + 1, hero.y], hero.x + 1, hero.y]
            if self.__cases[hero.x - 1, hero.y] != ' . ':
                return [self.__cases[hero.x - 1, hero.y], hero.x - 1, hero.y]
            if self.__cases[hero.x, hero.y + 1] != ' . ':
                return [self.__cases[hero.x, hero.y + 1], hero.x, hero.y + 1]
            if self.__cases[hero.x, hero.y - 1] != ' . ':
                return [self.__cases[hero.x, hero.y - 1], hero.x, hero.y - 1]
            else:
                return 0
        else:
            return -1

    def showMap(self):
        for i in range(15):
            print(self.__cases[i])

                    