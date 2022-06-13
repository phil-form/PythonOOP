from datetime import date, datetime
from Models.Course import Course

def plongerDansLesPiecesDor():
    print("YOUPIII")

class Teacher:
    def __init__(self, firstname: str, lastname: str, hireDate: date, email: str) -> None:
        self.__firstname = firstname
        self.__lastname = lastname
        self.__hireDate = hireDate
        self.__email = email
    
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

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value: str):
        self.__email = value

    @property
    def hireDate(self):
        return self.__hireDate

    @hireDate.setter
    def hireDate(self, value: date):
        self.__hireDate = value

    def teach(self, course: Course):
        print(self.__firstname + " " + self.__lastname + " teach : " + course.name)

    def __str__(self) -> str:
        return f"{self.__firstname} {self.__lastname}"

    # def __repr__(self) -> str:
    #     return f"Teacher : {self.__firstname} {self.__lastname}"