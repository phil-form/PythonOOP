from datetime import datetime
from Models.Animal import Animal

class Chat(Animal):
    def __init__(self, nom: str, poids: int, taille: int, 
        sexe: bool, age: int, dateDArriveee: datetime,
        caractere: str, griffeCoupee: bool, poilLong: bool) -> None:
        super().__init__(nom, poids, taille, sexe, age, dateDArriveee, 5, "meow")
        self.__caractere = caractere
        self.__griffeCoupee = griffeCoupee
        self.__poilLong = poilLong

    @property
    def caractere(self):
        return self.__caractere

    @caractere.setter
    def caractere(self, value: str):
        self.__caractere = value

    @property
    def griffeCoupee(self):
        return self.__griffeCoupee

    @griffeCoupee.setter
    def griffeCoupee(self, value: bool):
        self.__griffeCoupee = value

    @property
    def poilLong(self):
        return self.__poilLong

    @poilLong.setter
    def poilLong(self, value: bool):
        self.__poilLong = value

    def crier(self):
        print("Meeow")