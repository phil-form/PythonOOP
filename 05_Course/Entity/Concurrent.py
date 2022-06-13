from Entity.Voiture import Voiture
from Entity.Circuit import Circuit

class Concurent:

    def __init__(self, name: str, number: int, car: Voiture) -> None:
        self.__name = name
        self.__number = number
        self.__car = car
        self.__lapTime = list()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value: int):
        self.__number = value

    @property
    def car(self):
        return self.__car

    @car.setter
    def car(self, value: Voiture):
        self.__car = value

    @property
    def lapTimes(self):
        return tuple(self.__lapTime)

    @property
    def totalTime(self) -> float:
        return sum(self.lapTimes)

    def doLap(self, circuit: Circuit):
        vit = self.car.getSpeed() / 3.6

        distance = circuit.length
        time = distance / vit

        self.__lapTime.append(time)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Concurent):
            return self.name == __o.name

        return False