class Classroom:
    def __init__(self, nbMax : int):
        self.__nbMax = nbMax
        self.__students = []

    def addStudent(self, student : Student):
        if isinstance(student, Student):
            if self.__nbMax < len(self.__students):
                self.__students.append(student)
            else: 
                print("La classe est pleine")