from random import randint
from models.board.coord import Coord

class Board:

    def __init__(self, size_x, size_y):
        self.__size_x = size_x
        self.__size_y = size_y
        self.__hero = None
        self.__monsters = []

    @property
    def sizeX(self):
        return self.__size_x

    @property
    def sizeY(self):
        return self.__size_y

    @property
    def monsters(self):
        return self.__monsters

    @monsters.setter
    def monsters(self, value):
        self.__monsters = value

    @property
    def hero(self):
        return self.__hero

    @hero.setter
    def hero(self, value):
        self.__hero = value

    def generateCoords(self) -> Coord :
        return Coord(randint(0, self.sizeX-1), randint(0, self.sizeY-1))

    def moveUp(self, char) -> bool:
        newY = char.posY + 1
        if newY > self.sizeY:
            return False
        else:
            char.posY = newY
            return True

    def moveDown(self, char) -> bool:
        newY = char.posY - 1
        if newY < 0:
            return False
        else:
            char.posY = newY
            return True

    def moveLeft(self, char) -> bool:
        newX = char.posX - 1
        if newX < 0:
            return False
        else:
            char.posX = newX
            return True

    def moveRight(self, char) -> bool:
        newX = char.posX + 1
        if newX > self.sizeX:
            return False
        else:
            char.posX = newX
            return True

    def monstersNextToHero(self):
        res = []
        for m in self.monsters:
            if not m.isDead() and (abs(self.hero.posX - m.posX) == 1 and self.hero.posY == m.posY) or (abs(self.hero.posY - m.posY) == 1 and self.hero.posX == m.posX):
                res.append(m)
        return res

    def monstersAtPos(self, x, y):
        for m in self.monsters:
            if m.posX == x and m.posY == y:
                return m
        return None

    def __str__(self):
        res = ""
        for y in range(self.sizeY-1, 0, -1):
            res += "\n"
            for x in range(self.sizeX):
                m = self.monstersAtPos(x, y)
                if self.hero.posX == x and self.hero.posY == y:
                    res += "H|"
                elif m != None:
                    res += f"{m.shortName()}|"
                else:
                    res += " |"
            res += "\n"
        return res