from abc import ABC, abstractmethod
from datetime import datetime

class Animal(ABC):
    def __init__(self, nom: str, poids: int, 
        taille: int, sexe: bool, age: int, 
        dateDArriveee: datetime, probaDeces: int, cri: str) -> None:
        self.__nom = nom
        self.__poids = poids
        self.__taille = taille
        self.__sexe = sexe
        self.__age = age
        self.__dateDArriveee = dateDArriveee
        self.__probaDeces = probaDeces
        self.__cri = cri

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value: str):
        self.__nom = value

    @property
    def poids(self):
        return self.__poids

    @poids.setter
    def poids(self, value: int):
        self.__poids = value

    @property
    def taille(self):
        return self.__taille

    @taille.setter
    def taille(self, value: int):
        self.__taille = value

    @property
    def sexe(self):
        return self.__sexe

    @sexe.setter
    def sexe(self, value: bool):
        self.__dateDArriveee = value

    @property
    def dateDArrivee(self):
        return self.__dateDArriveee

    @dateDArrivee.setter
    def dateDArrivee(self, value: datetime):
        self.__dateDArriveee = value

    @property
    def probaDeces(self):
        return self.__probaDeces

    @abstractmethod
    def crier(self):
        pass
        # print(self.__cri)

    def __str__(self) -> str:
        return f"{self.__nom} {self.__poids} {self.__age}"