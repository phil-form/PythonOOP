class Teacher:

    def __init__(self, nom, prenom, age, email):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
        self.__email = email

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
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        self.__email = value

prof1 = Teacher("Jules", "Maverick", 24, "jules.test@maverick.be")
print(prof1.nom)