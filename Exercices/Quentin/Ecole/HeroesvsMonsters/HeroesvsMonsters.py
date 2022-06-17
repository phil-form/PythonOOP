from abc import ABC, abstractmethod
from random import randint


class Characters() :
    def __init__():
        self.__Force = self.ForceEnd()
        self.__Endurance = self.ForceEnd()
        self.__PointdeVies= self.PointdeVies()


    @property
    def Force (self):
        return self.__Force

    def ForceEnd (self):
        tab =[]
        for i in range(0,3):
          tab.append(Dice.Lance(6))
        tab.sort()
        del tab[0]
        return sum(tab)        
    

    @property
    def Endurance(self):
        return self.__Endurance

    @property()
    def PointdeVies (self):
        return self.__PointdeVies

    @PointdeVies.setter
    def PointdeVies(self):
        pdv = self.__Endurance
        if pdv < 5 :
            self.__PointdeVies = pdv -1
        elif pdv < 10 and pdv > 15:
            self.__PointdeVies = pdv + 1
        elif pdv > 15 :
            self.__PointdeVies = pdv + 2
        

    def frappe():
        dega = 0
        forc = self.__Force
        result = Dice.Lance(4)
        score = forc + result
        if score < 5 :
            dega = score - 1
        elif pdv < 10 and pdv > 15:
            dega = score + 1
        elif pdv > 15 :
            dega = score + 2
        


class Humain(Characters) :

    @property
    def Endurance(self):
        return super().Endurance + 1
    
    @property
    def Force(self):
        return super().Force + 1


class Nain(Characters):

    @property
    def Endurance(sel):
        return super().Endurance + 2
    

class Monsters() :
    pass

class Dice() :

    def __init__(self):
        self.__Min = 1
        self.__Max = Maxi
        
    def Lance(self):
        return randint(self.__Min,self.__Max)