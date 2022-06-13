from random import randint

class Voiture:
    def __init__(self, brand: str, model: str, minSpeed: int, maxSpeed: int) -> None:
        self.brand = brand
        self.model = model
        self.minSpeed = minSpeed
        self.maxSpeed = maxSpeed

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value: str):
        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value: str):
        self.__model = value
    
    @property
    def minSpeed(self):
        return self.__minSpeed

    @minSpeed.setter
    def minSpeed(self, value: int):
        self.__minSpeed = value

    @property
    def maxSpeed(self):
        return self.__maxSpeed

    @maxSpeed.setter
    def maxSpeed(self, value: int):
        self.__maxSpeed = value

    def getSpeed(self):
        return randint(self.minSpeed, self.maxSpeed)

    def __str__(self) -> str:
        return f"{self.model} {self.brand}"