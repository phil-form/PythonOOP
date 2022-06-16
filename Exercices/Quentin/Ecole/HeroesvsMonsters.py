from abc import ABC, abstractmethod
from random import randint


class Characters(Dice) :
    def __init__(For,End, PV, race):
        super().__init__()
        self.__Force = For
        self.__Endurance = End
        self.__PointdeVies= PV
        self.__Races = race

    @property
    def Force (self):
        return self.__Force
    
    def ForceEnd (self):
        tab =[]
        for i in range(0,3):
          tab.append(Lance(mini,maxi))
        tab.sort()
        del tab[0]
        EndFor = sum(tab)
        self.__Force = EndFor
        self.__Endurance = EndFor

    @property
    def Endurance(self):
        return self.__Endurance

    @property()
    def PointdeVies (self):
        return self.__PointdeVies

    @PointdeVies.setter
    def PointdeVies(self, value):
        self.__PointdeVies = Value

    @property
    def Races(self):
        return self.__Races

    @Races.setter
    def Races(self,Value):
        self.__Races = Value

    def frappe():
        return Lance()


class Humain() :
    pass

class Monsters() :
    pass

class Dice() :

    def __init__(Maxi):
        self.__Min = 1
        self.__Max = Maxi
        
    def Lance(self):
        return randint(self.__Min,self.__Max)