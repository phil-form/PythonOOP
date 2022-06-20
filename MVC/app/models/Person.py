class Experience:
    def __init__(self, date, name) -> None:
        self.date = date
        self.name = name

class Person:
    def __init__(self, firstname, lastname, title) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.experiences = []
        self.skills = []
        self.formation = []

    def addExperience(self, date, name):
        self.experiences.append(Experience(date, name))

    def addSkills(self, name):
        self.skills.append(name)

    def addFormation(self, name):
        self.formation.append(name)