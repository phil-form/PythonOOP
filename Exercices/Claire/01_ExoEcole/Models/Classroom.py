from random import randint, random
from Models.Teacher import Teacher
from Models.Student import Student
from Models.Course import Course

class Classroom:
    def __init__(self, nbPlace: int) -> None:
        self.__maxStudent = nbPlace
        self.__students = []
        self.__mainTeacher = None

    def addStudent(self, student: Student):
        if isinstance(student, Student):
            if self.__maxStudent > len(self.__students):
                self.__students.append(student)
            else:
                print("La classe est complete")

    def startCourse(self, course: Course, teacher: Teacher):
        teacher.teach(course)

        for student in self.__students:
            if randint(0, 10) > 2:
                student.go_to_class(course)
            else:
                student.skip_class()
