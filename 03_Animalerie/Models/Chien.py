from datetime import datetime
from Models.Animal import Animal

class Chien(Animal):
    def __init__(self, nom: str, poids: int, taille: int, 
        sexe: bool, age: int, dateDArriveee: datetime,
        couleurColier: str, dresser: bool, race: str) -> None:
        super().__init__(nom, poids, taille, sexe, age, dateDArriveee, 3, "Wouf")
        self.__couleurColier = couleurColier
        self.__dresser = dresser
        self.__race = race

    @property
    def couleurColier(self):
        return self.__couleurColier

    @couleurColier.setter
    def couleurColier(self, value: str):
        self.__couleurColier = value

    @property
    def dresser(self):
        return self.__dresser

    @dresser.setter
    def dresser(self, value: bool):
        self.__dresser = value

    @property
    def race(self):
        return self.__race

    @race.setter
    def race(self, value: str):
        self.__race = value

    def crier(self):
        print("Whouf")