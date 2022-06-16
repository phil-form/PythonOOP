class Student:

    def __init__(self, nom, prenom, naissance):
        self.__nom = nom
        self.__prenom = prenom
        self.__naissance = naissance

    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def prenom(self):
        return self.__prenom
    
    @prenom.setter
    def prenom(self, value):
        self.__prenom = value
        
    @property
    def matr(self):
        return self.__nom[:3] + self.__prenom[:3]

    @property
    def naissance(self):
        return self.__naissance
    
    @naissance.setter
    def naissance(self, value):
        self.__naissance = value

stud1 = Student("Jules", "Maverick", "16/02/1996")
print(stud1.matr)