from inspect import getcomments
from random import randrange
from Monsters import Wolf, Orc, Dragonling
from Heroes import Human, Dwarf
import os

class Map:
	def __init__(self, monster_count):
		self.hero_pos = [0, 0]
		self.map = []
		self.monsters = []
		self.hero = self.map_init(monster_count)

	def map_init(self, monster_count):
		inpt = int(input("Select a hero:\n1) Human (+1 str, +1 stam)\n2) Dwarf (+2 stam)\n"))
		name = input("What's your hero's name ?\n")
		hero = None
		if inpt == 1:
			hero = Human(name)
		else:
			hero = Dwarf(name)

		for i in range(15):
			row = []
			for j in range(15):
				row.append(0)
			self.__map.append(row)

		for i in range(monster_count):
			x = randrange(15)
			y = randrange(15)
			while not self.checkAround(x, y, 2):
				x = randrange(15)
				y = randrange(15)
			self.__map[y][x] = self.generateRandomMonster()
			self.monsters.append(self.__map[y][x])

		x = randrange(15)
		y = randrange(15)
		while not self.checkAround(x, y, 2):
			x = randrange(15)
			y = randrange(15)
		self.hero_pos[0] = y
		self.hero_pos[1] = x
		return hero
	
	def generateRandomMonster(self):
		rand = randrange(3)
		if rand == 0:
			return Wolf("Young timber wolf")
		elif rand == 1:
			return Orc("Garrosh Hellscream")
		else:
			return Dragonling("Nefarian")

	def checkAround(self, x, y, size):
		for hor in range(max(0, x - size), min(15, x + size + 1)):
			for ver in range(max(0, y - size), min(15, y + size + 1)):
				if not self.__map[ver][hor] == 0:
					return False
		return True

	def show(self):
		print(f"\033[33;1mGold: {self.hero.gold}\033[0m")
		print(f"leather: {self.hero.leather}")
		for i in range(15):
			for j in range(15):
				if i == self.hero_pos[0] and j == self.hero_pos[1]:
					print(f"\033[1;34mH\033[0m", end=" ")
				elif not self.__map[i][j] == 0:
					print(f"\033[1;31m{type(self.__map[i][j]).__name__[0]}\033[0m", end=" ")
				else:
					print(0, end=" ")
			print()
		print()

	def play(self):
		while self.hero.hp > 1 and len(self.monsters):
			os.system('clear')
			self.show()
			move = input()
			self.move(move)
			if not self.checkAround(self.__hero_pos[1], self.__hero_pos[0], 1):
				self.fight()
		if self.hero.hp > 1:
			print("You won!")
		else:
			print("You lost!")

	def move(self, direction):
		if direction.upper() == "A":
			self.__hero_pos[1] = max(0, self.__hero_pos[1] - 1)
		if direction.upper() == "D":
			self.__hero_pos[1] = min(14, self.__hero_pos[1] + 1)
		if direction.upper() == "W":
			self.__hero_pos[0] = max(0, self.__hero_pos[0] - 1)
		if direction.upper() == "S":
			self.__hero_pos[0] = min(14, self.__hero_pos[0] + 1)

	def fight(self):
		monsters = self.getMonsters()
		for monster in monsters:
			self.fightMonster(monster[0], monster[1], monster[2])

	def fightMonster(self, monster, y, x):
		while self.hero.hp > 0 and monster.hp > 0:
			os.system('clear')
			print(f"{self.hero.name:<15} {monster.name} ({type(monster).__name__})")
			print(f"{self.hero.hp}/{self.hero.hpMax}  {monster.hp:>11}/{monster.hpMax}")
			print("___________________________________________")
			self.hero.strike(monster)
			if monster.hp < 1:
				os.system('clear')
				continue
			monster.strike(self.hero)
			input()
		print(f"{self.hero.name:<15} {monster.name} ({type(monster).__name__})")
		print(f"{self.hero.hp}/{self.hero.hpMax}  {monster.hp:>11}/{monster.hpMax}")
		print("___________________________________________")
		input()
		os.system('clear')
		if (monster.hp < 1):
			print(f"{self.hero.name} killed {monster.name}!")
			self.hero.skin(monster)
			self.hero.loot(monster)
			self.hero.regen()
			self.map[y][x] = 0
			self.monsters.remove(monster)
			input()
		else:
			print(f"{self.hero.name} got killed by {monster.name}!")


	def getMonsters(self):
		y = self.__hero_pos[0]
		x = self.__hero_pos[1]
		rval = []
		if not self.map[max(y - 1, 0)][x] == 0:
			rval.append((self.__map[y - 1][x], y - 1, x))

		if not self.map[min(y + 1, 14)][x] == 0:
			rval.append((self.__map[y + 1][x], y + 1, x))

		if not self.map[y][max(0, x - 1)] == 0:
			rval.append((self.__map[y][x - 1], y, x - 1))

		if not self.map[y][min(14, x + 1)] == 0:
			rval.append((self.__map[y][x + 1], y, x + 1))
		return rval

	@property
	def map(self):
		return self.__map
	@map.setter
	def map(self, val):
		self.__map = val

	@property
	def hero(self):
		return self.__hero
	@hero.setter
	def hero(self, val):
		self.__hero = val

	@property
	def hero_pos(self):
		return self.__hero_pos
	@hero_pos.setter
	def hero_pos(self, val):
		self.__hero_pos = val

	@property
	def monsters(self):
		return self.__monsters
	@monsters.setter
	def monsters(self, val):
		self.__monsters = val
	
if __name__ == "__main__":
	map = Map(5)
	map.play()