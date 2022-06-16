from datetime import date
from Models.Course import Course
from Models.Student import Student
from Models.Classroom import Classroom
from Models.Teacher import Teacher, plongerDansLesPiecesDor

plongerDansLesPiecesDor()

print(Teacher.__name__)
print(Teacher.__bases__)
print(Teacher.__class__)

balthazar = Teacher("Balthazar", "Picsou", date(1947, 1, 1), "super.picsou@picsou.pognon")
print(balthazar.__class__)
print(balthazar.__dict__)
print(balthazar)
riri = Student("Riri", "Duck", date(1997, 1, 1), 2)
loulou = Student("Loulou", "Duck", date(1997, 1, 1), 1)

compta = Course("Comptabilité")

classRoom = Classroom(5)
classRoom.addStudent(riri)
classRoom.addStudent(loulou)
classRoom.startCourse(compta, balthazar)