from random import randrange
class Dice:
	def __init__(self, min, max):
		self.__min = min
		self.__max = max

	def roll(self):
		return randrange(self.min, self.max + 1)

	def rollStat(self, RollCount):
		rolls = []
		for i in range(RollCount):
			rolls.append(self.roll())
		rolls.remove(min(rolls))
		return sum(rolls)

	
	@property
	def min(self):
		return self.__min

	@property
	def max(self):
		return self.__max

if __name__ == "__main__":
	dice = Dice(1, 4)
	print("4 faced dice:")
	for i in range(10):
		print(dice.roll())
	print()
	dice = Dice(1, 6)
	print("6 faced dice:")
	for i in range(10):
		print(dice.roll())
	print()
	print(dice.rollStat(1))

	for i in range(10):
		print(randrange(15))
