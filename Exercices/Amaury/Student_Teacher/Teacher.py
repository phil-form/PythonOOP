from Personn import Personn

class Teacher(Personn):
    def __init__(self, firstname, lastname, age, lessons = [], classrooms = []):
        super().__init__(firstname, lastname, age)
        self.__lessons = lessons
        self.__classrooms = []

    def _addLesson(self, lesson):
        self.__lessons.append(lesson)

    def _removeLesson(self, lesson):
        self.__lessons.remove(lesson)

    def _addClasse(self, classroom):
        self.__classrooms.append(classroom)

    def _removeClasse(self, classroom):
        self.__classrooms.remove(classroom)

    def __str__(self):
        print(f"{self.firstname} {self.lastname}, {self.age} years old. Lessons: {self.lessons}")