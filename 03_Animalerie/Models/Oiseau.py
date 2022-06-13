from datetime import datetime
from Models.Animal import Animal

class Oiseau(Animal):
    def __init__(self, nom: str, poids: int, taille: int, 
        sexe: bool, age: int, dateDArriveee: datetime,
        couleur: str, voliere: bool) -> None:
        super().__init__(nom, poids, taille, sexe, age, dateDArriveee, 10, "Quiqui")
        self.__couleur = couleur
        self.__voliere = voliere

    @property
    def couleur(self):
        return self.__couleur

    @couleur.setter
    def couleur(self, value: str):
        self.__couleur = value

    @property
    def voliere(self):
        return self.__voliere

    @voliere.setter
    def voliere(self, value: bool):
        self.__voliere = value

    def crier(self):
        print("Quiqui")