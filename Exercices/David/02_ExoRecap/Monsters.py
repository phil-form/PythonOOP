from Character import Character
from random import randrange
class Monster(Character):
	pass

class Wolf(Monster):
	def __init__(self, name):
		super().__init__(name)
		self.skinned = False

	@property
	def skinned(self):
		return self.__skinned

	@skinned.setter
	def skinned(self, bool):
		self.__skinned = bool

class Orc(Monster):
	def __init__(self, name):
		super().__init__(name)
		self.gold = randrange(10)
		self.leather = randrange(10)
	@property
	def strength(self):
		return super().strength + 1

class Dragonling(Monster):
	def __init__(self, name):
		super().__init__(name)
		self.gold = randrange(10)
		self.skinned = False

	@property
	def skinned(self):
		return self.__skinned

	@skinned.setter
	def skinned(self, bool):
		self.__skinned = bool

	@property
	def strength(self):
		return super().stamina + 1