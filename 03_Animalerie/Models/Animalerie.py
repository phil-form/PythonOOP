from random import random

from numpy import isin
from Models.Animal import Animal
from Models.Chat import Chat
from Models.Chien import Chien
from Models.Oiseau import Oiseau
from random import randrange
from Toolbox.Inputs import readInt, readBool, readDate, readStr

class Animalerie:
    def __init__(self) -> None:
        self.__animaux = []
        self.__catCount = 0
        self.__dogCount = 0
        self.__birdCount = 0

    def addAnimal(self):
        choice = 0
        while choice > 3 or choice < 1:
            choice = readInt("Entrer 1 => chat 2 => chien 3 => oiseau : ")

        nom = readStr("Entrer le nom : ")
        poids = readInt("Entrer le poids : ")
        taille = readInt("Entrer le taille : ")
        age = readInt("Entrer l'age : ")
        sexe = readBool("Entrer le sexe : ")
        dateDarrivee = readDate("Entrer la date d'arrivée : ")

        animal = None

        if choice == 1:
            caractere = readStr("Entrer le caractere : ")
            griffeCoupee = readBool("Entrer si il a les griffes coupées : ")
            poilLong = readBool("Entrer si il a les poils longs : ")

            animal = Chat(nom, poids, taille, sexe, age, 
                dateDarrivee, caractere, griffeCoupee, poilLong)

            self.__catCount += 1

        elif choice == 2:
            couleurCollier = readStr("Entrer la couleur du collier : ")
            race = readStr("Entrer la race : ")
            dresser = readBool("Entrer si il est dresser : ")

            animal = Chien(nom, poids, taille, sexe, age, 
                dateDarrivee, couleurCollier, dresser, race)

            self.__dogCount += 1

        elif choice == 3:
            couleur = readStr("Entrer la couleur : ")
            voliere = readBool("Entrer si il est en voliere : ")

            animal = Oiseau(nom, poids, taille, sexe, age, 
                dateDarrivee, couleur, voliere)

            self.__birdCount += 1

        self.__animaux.append(animal)

    def listAnimals(self):
        for animal in self.__animaux:
            print(animal)

    def showNumbers(self):
        print(f"cats : {self.__catCount} dogs : {self.__dogCount} birds {self.__birdCount}")

    def passerNuit(self):
        for animal in self.__animaux:
            if animal.probaDeces > randrange(100):
                print(animal.nom + " est mort :,(")
                self.__animaux.remove(animal)

                if isinstance(animal, Chat):
                    self.__catCount = self.__catCount - 1 if self.__catCount > 1 else 0
                if isinstance(animal, Chien):
                    self.__dogCount = self.__dogCount - 1 if self.__dogCount > 1 else 0
                if isinstance(animal, Oiseau):
                    self.__birdCount = self.__birdCount - 1 if self.__birdCount > 1 else 0

    def coucou(self, animal: Animal):
        animal.crier()