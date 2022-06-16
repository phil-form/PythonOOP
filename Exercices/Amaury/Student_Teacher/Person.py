

class Personn:
    def __init__(self, firstname, lastname, age):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age

        @property
        def firstname(self):
            return self.__firstname

        @firstname.setter
        def firstname(self, value):
            self.__firstname = value

        @property
        def lastname(self):
            return self.__lastname

        @lastname.setter
        def lastname(self, value):
            self.__lastname = value

        @property
        def age(self):
            return self.__age

        @age.setter
        def age(self, value):
            self.__age = value