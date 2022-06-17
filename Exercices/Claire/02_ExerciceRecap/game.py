from models.heroes.hero import Hero
from models.heroes.human import Human
from models.heroes.dwarf import Dwarf
from models.monsters.dragon import Dragon
from models.monsters.orc import Orc
from models.monsters.wolf import Wolf
from models.board.board import Board
from exceptions.invalid_move import InvalidMove
from random import randint


class Game():

    def __init__(self, size_x = 15, size_y = 15, nMonsters = 10):
        self.__board = Board(size_x, size_y)
        self.__hero = self.generateHero()
        self.__monsters = self.generateMonsters(nMonsters)
        self.__board.monsters = self.__monsters
        self.__board.hero = self.hero
        self.__nDefeated = 0
    
    @property
    def board(self):
        return self.__board
    
    @property
    def hero(self):
        return self.__hero
    
    @property
    def monsters(self):
        return self.__monsters

    def start(self):
        finished = False
        while not finished:
            print(self.board)
            self.moveManagement()

            monsters = self.board.monstersNextToHero()
            if len(monsters) > 0:
                for m in monsters:
                    self.fightMonster(m)
                    if not self.hero.isDead():
                        self.hero.resetHp()
            finished = self.isGameEnded()
            
    def isGameEnded(self):
        if self.hero.isDead():
            self.lost()
            return True
        
        allDead = True
        for m in self.monsters:
            if not m.isDead():
                allDead = False
        if allDead:
            self.win()
            return True    
        return False
            
    def fightMonster(self, monster):
        finished = False
        while not finished:
            self.hero.doAttack(monster)
            if not monster.isDead():
                monster.doAttack(self.hero)
            else:
                self.hero.loot(monster)
            finished = self.hero.isDead() or monster.isDead()
        
            

    def win(self):
        print(f"Hero won, {self.nDefeated+1} monsters defeated. Hero has {self.hero.gold} golds and {self.hero.leather} leathers")

    def lost(self):
        print("Hero lost !")

    def generateHero(self):
        hero = randint(1, 2)
        coords = self.board.generateCoords()
        if hero == 1:
            return Dwarf("Nova", coords.x, coords.y)
        elif hero == 2:
            return Human("Nova", coords.x, coords.y)

    def generateMonsters(self, nbr):
        monsters = []
        for i in range(nbr):
            monster = randint(1, 3)
            coords = self.board.generateCoords()
            if monster == 1:
                monsters.append(Dragon(coords.x, coords.y))
            elif monster == 2:
                monsters.append(Orc(coords.x, coords.y))
            elif monster == 3:
                monsters.append(Wolf(coords.x, coords.y))
        return monsters

    def moveManagement(self):
        move = input("Where do you want to go (use arrows) ?")
        if move == "\x1b[A": # up
            self.board.moveUp(self.hero)
        elif move == "\x1b[B": # down
            self.board.moveDown(self.hero)
        elif move == "\x1b[C": # right
            self.board.moveRight(self.hero)
        elif move == "\x1b[D": #left
            self.board.moveLeft(self.hero)
        else:
            raise(InvalidMove())

    

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()