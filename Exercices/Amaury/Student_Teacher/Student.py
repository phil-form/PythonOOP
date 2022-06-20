from Personn import Personn

class Student(Personn):
    def __init__(self, firstname, lastname, age, birthday):
        super().__init__(firstname, lastname, age)
        self.birthday = birthday
        self.lessons = {}

    def isPresent(self, lesson, date):
        self.lessons[lesson].append[date, True]

    def isAbsent(self, lesson, date):
        self.lessons[lesson].append[date, False]