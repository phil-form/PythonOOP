from abc import ABC, abstractmethod

class Personne(ABC):
    def __init__(self, firstname,lastname):
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

class Teacher:
    def __init__(self, firstname: str, lastname: str, hireDate: date, email: str) -> None:
        super().__init__(firstname,lastname)
        self.__firstname = firstname
        self.__lastname = lastname
        self.__hireDate = hireDate
        self.__email = email