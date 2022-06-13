from datetime import date, datetime
from Models.Course import Course
from Models.Person import Person

class Teacher(Person):
    def __init__(self, firstname: str, lastname: str, hireDate: date, email: str) -> None:
        super().__init__(firstname, lastname)
        self.__hireDate = hireDate
        self.__email = email
    
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
        print(self.firstname + " " + self.lastname + " teach : " + course.name)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"
