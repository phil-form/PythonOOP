import math
import os
from time import sleep, time
from models.Hero.Dwarf import Dwarf
from models.Hero.Human import Human
from models.Monster.Dragon import Dragon
from models.Monster.Orc import Orc
from models.Monster.Wolf import Wolf
from models.Monster.Monster import Monster
from models.Coordinate import Coordinate
from models.Character import Character
from enums.Direction import Direction
from toolBox.Dice import Dice
import keyboard

class Forest():
    def __init__(self, size = 15, nbMonster = 15) -> None:
        self.__size = size
        self.__characters = []
        self.__initMonsters(nbMonster)
        self.__hero = self.__initPlayer()
        self.__characters.append(self.__hero)
        self.__ennemyCount = nbMonster
        print(self.__hero)

    def __initPlayer(self):
        race = 2
        while race == None:
            try:
                choice = int(input("Choice between human (1) or Dwarf (2) : "))
                
                if(choice == 1 or choice == 2):
                    race = choice

                else:
                    raise ValueError()

            except ValueError:
                print("Incorrect input enter either 1 or 2!")

        heroName = input("Enter your character name : ")
        coor = self.__getValidCoord()
        return Human(heroName, coor) if race == 1 else Dwarf(heroName, coor)

    def __initMonsters(self, nbMonster):
        dice3 = Dice(3)

        for i in range(nbMonster):
            monsterChoice = dice3.throw()
            coord = self.__getValidCoord()

            if monsterChoice == 1:
                self.__characters.append(Wolf(coord))
            elif monsterChoice == 2:
                self.__characters.append(Orc(coord))
            else:
                self.__characters.append(Dragon(coord))

    def __getValidCoord(self):
        dice = Dice(self.__size)

        x, y = 0, 0

        isPlaced = False

        while(not isPlaced):
            x, y = dice.throw() - 1, dice.throw() - 1

            isPlaced = True

            mnstr: Character
            for mnstr in self.__characters:
                if abs(mnstr.coorX - x) < 3 and abs(mnstr.coorY - y) < 3:
                    isPlaced = False

        return Coordinate(x, y)

    def __characterMoved(self):
        moved = False
        if keyboard.is_pressed("w") or keyboard.is_pressed("up"):
            if self.__hero.coorX > 0:
                self.__hero.move(Direction.NORTH)
                moved = True
        if keyboard.is_pressed("s") or keyboard.is_pressed("down"):
            if self.__hero.coorX < self.__size - 1:
                self.__hero.move(Direction.SOUTH)
                moved = True
        if keyboard.is_pressed("a") or keyboard.is_pressed("left"):
            if self.__hero.coorY > 0:
                self.__hero.move(Direction.WEST)
                moved = True
        if keyboard.is_pressed("d") or keyboard.is_pressed("right"):
            if self.__hero.coorY < self.__size - 1:
                self.__hero.move(Direction.EAST)
                moved = True

        return moved

    def __getIndexToken(self, coor: Coordinate):
        if self.__hero == coor:
            return self.__hero.getToken()

        ch: Character
        for ch in self.__characters:
            if ch == coor:
                return ch.getToken()

        return ' * '

    def __printMap(self):
        for i in range(self.__size):
            for j in range(self.__size):
                coord = Coordinate(i, j)
                print(self.__getIndexToken(coord), end='')

            print()

    def __getNearestMonster(self):
        hero = self.__hero

        for char in self.__characters:
            if isinstance(char, Monster) and char.coorX == hero.coorX and char.coorY == hero.coorY:
                return char

        return None

    def __fight(self, monster: Monster):
        dice2 = Dice(2)
        hero = self.__hero
        monster.hidden = False

        if monster.isDead():
            return

        init = dice2.throw() == 1
        while not hero.isDead() and not monster.isDead():
            if init:
                hero.hit(monster)
            else:
                monster.hit(hero)

            init = not init

        if not hero.isDead():
            print(f"{hero.name} won against {monster.race}")
            hero.loot(monster)
            hero.rest()
            hero.killCount += 1

        print()
        sleep(1)

    def play(self):
        self.__printMap()
        while not self.__hero.isDead() and self.__hero.killCount < self.__ennemyCount:
            if self.__characterMoved():
                os.system('clear')
                self.__printMap()
                monster = self.__getNearestMonster()
                if monster != None:
                    self.__fight(monster)
                sleep(0.25)

        if(self.__hero.isDead()):
            print("RIP")
        print(f"You won : {self.__hero.getGold()} golds and {self.__hero.getLeather()} leathers")