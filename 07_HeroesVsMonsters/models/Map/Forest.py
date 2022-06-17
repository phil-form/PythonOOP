from models.Hero.Dwarf import Dwarf
from models.Hero.Human import Human
from models.Monster.Dragon import Dragon
from models.Monster.Orc import Orc
from models.Monster.Wolf import Wolf
from toolBox.Dice import Dice

class Forest():
    def __init__(self) -> None:
        self.__hero = self.__initPlayer()
        print(self.__hero)

    def __initPlayer(self):
        race = None
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

        return Human(heroName) if race == 1 else Dwarf(heroName)

    def play(self):
        hero = self.__hero
        dice2 = Dice(2)
        dice3 = Dice(3)

        while not hero.isDead():
            monsterChoice = dice3.throw()

            monster = None
            if monsterChoice == 1:
                monster = Wolf()
            elif monsterChoice == 2:
                monster = Orc()
            else:
                monster = Dragon()

            print(f"You encounter  a : {monster.race} !")

            init = dice2.throw() == 1
            while not hero.isDead() and not monster.isDead():
                if init:
                    hero.hit(monster)
                    print(f"You're attacking! {monster.health}")
                else:
                    monster.hit(hero)
                    print(f"The monster attacks! {hero.health}")

                init = not init

            if not hero.isDead():
                print(f"{hero.name} won against {monster.race}")
                hero.loot(monster)
                hero.rest()

            print()
        
        print("RIP")
        print(f"You won : {hero.getGold()} golds and {hero.getLeather()} leathers")