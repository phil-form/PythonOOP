class Person:
	def __init__(self, firstname, lastname) -> None:
		self.__firstname = firstname
		self.__lastname = lastname

	@property
	def firstname(self):
		return self.__firstname

	@firstname.setter
	def firstname(self, value: str):
		self.__firstname = value

	@property
	def lastname(self):
		return self.__lastname

	@lastname.setter
	def lastname(self, value: str):
		self.__lastname = value