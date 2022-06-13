from datetime import date
from Models.Course import Course

class Student:
    def __init__(self, firstname: str, lastname: str, birthdate: date, grade: int) -> None:
        self.__firstname = firstname
        self.__lastname = lastname
        self.__birthdate = birthdate
        self.__grade = grade
    
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
    def birthdate(self):
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, value: date):
        self.__birthdate = value

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value: int):
        self.__grade = value

    @property
    def matricule(self):
        return self.__firstname[:3] + self.__lastname[:3]

    def skip_class(self):
        print(f"{self.firstname} {self.lastname} sèche les cours")

    def go_to_class(self, course: Course):
        print(f"{self.firstname} {self.lastname} participe aux cours {course.name}")