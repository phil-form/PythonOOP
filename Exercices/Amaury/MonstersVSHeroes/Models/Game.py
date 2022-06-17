import random
from Board import Board
from Hero import Hero

class Game():

    def __init__(self):
        self.__board = Board()
        self.__hero = Hero()
        self.__difficulty = 0

    @property
    def board(self):
        return self.__board

    @property
    def difficulty(self):
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, value):
        self.__difficulty = value

    def start(self):
        board = Board()
        board.addMonsters(difficulty)
        board.setHeroOnMap(self.__hero)
        while self.checkMonstersOnMap() != 0:
            self.__hero.move()
            action = board.setHeroOnMap(self.__hero)
            if action == -1:
                print('out of the map !')
                self.__hero.move()
            if action == 0:
                print('the hero is moving ...')
                self.__hero.move()
            else:
                print("oooo a monster, let's fight bastard")
                res = self.fight(self.__hero, action)
                if res == 0:
                    print('aaaaa... my honor is lost .... !')
                    print('The hero is dead')
                    print('GAME OVER')
                    break
        print('Well played !!! The forest is yours !!!')
        print('YOU WON')

    def fight(hero, monster):
        initiative = random.randint(1, 2)
        while monster[0].hp != 0 and hero.hp != 0:
            lst = hero
            nxt = monster[0]
            if initiative == 2:
                lst = monster[0]
                nxt = hero

            nxt.hp -= lst.force
            
            temp = lst
            lst = nxt
            nxt = temp

        if monster[0].hp == 0:
            return 1
        else:
            return 0

    def checkMonstersOnMap(self):
        count = 0
        for i in range(15):
            for j in range(15):
                if self.__board.cases[i][j] != ' . ':
                    count += 1
        
        count -= 1
        return count


            


