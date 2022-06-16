from Dice import Dice
class Character:
	def __init__(self, name):
		dice = Dice(1, 6)
		self.__name		= name
		self.__stamina	= dice.rollStat(4)
		self.__strength	= dice.rollStat(4)
		self.__hpMax	= self.stamina + self.__modifier(self.stamina)
		self.__hp		= self.__hpMax
		self.__gold		= 0
		self.__leather	= 0

	def __modifier(self, stat: int):
		if stat < 5:
			if stat > 1:
				return -1
		elif stat < 10:
			return 0
		elif stat < 15:
			return 1
		else:
			return 2

	def strike(self, target):
		if target.hp < 1:
			print(f"{target.name} is already dead")
			return 1
		dice = Dice(1, 4)
		dmg = dice.roll()
		dmg += self.__modifier(self.strength)
		print(f"{self.name} strikes {target.name} for {dmg}!")
		target.hp -= dmg
		return 0

	def loot(self, target):
		if target.hp < 1:
			self.gold	 += target.gold
			self.leather += target.leather
			print(f"{self.name} looted {target.gold} gold and {target.leather} from {target.name}")
			target.gold		= 0
			target.leather	= 0

	def skin(self, target):
		if  type(target).__name__ in ["Wolf", "Dragonling"]  and target.skinned == False:
			roll = Dice(1,3).roll()
			self.leather += roll
			target.skinned = True
			print(f"{self.name} skinned {roll} leather from {target.name}")
		else:
			print(f"you can't skin a {type(target).__name__}")

	def regen(self):
		self.hp = self.hpMax

	def __str__(self):
		return f"{self.name} ({self.hp}/{self.hpMax}):\n  type: {type(self).__name__}\n  stam: {self.stamina:>2}\n  str: {self.strength:>3}"

	@property
	def stamina(self):
		return self.__stamina
	
	@property
	def strength(self):
		return self.__strength

	@property
	def hpMax(self):
		return self.__hpMax

	@property
	def gold(self):
		return self.__gold
	@gold.setter
	def gold(self, val):
		self.__gold = val

	@property
	def leather(self):
		return self.__leather
	@leather.setter
	def leather(self, val):
		self.__leather = val

	@property
	def racial(self):
		return self.__racial
	@racial.setter
	def racial(self, bonus):
		self.__racial = bonus

	@property
	def hp(self):
		return self.__hp
	@hp.setter
	def hp(self, val):
		self.__hp = val
		if val < 0:
			self.__hp = 0

	@property
	def name(self):
		return self.__name
	@name.setter
	def name(self, val):
		self.__name = val

if __name__ == "__main__":
	char1 = Character("Claire")
	char2 = Character("Amaury")
	print(char1, char2, sep="\n")
	while not char1.strike(char2):
		print(char1, char2, sep="\n")
	print(char1, char2, sep="\n")