from Character import Character

class Hero(Character):
	pass

class Human(Hero):
	@property
	def stamina(self):
		return super().stamina + 1
	
	@property
	def strength(self):
		return super().strength + 1

class Dwarf(Hero):
	@property
	def stamina(self):
		return super().stamina + 2