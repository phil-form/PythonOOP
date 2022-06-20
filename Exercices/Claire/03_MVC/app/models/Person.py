class Person:

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__descr = None
        self.__experiences = []
        self.__skills = []
        self.__training = None

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def descr(self):
        return self.__descr

    @descr.setter
    def descr(self, value: str):
        self.__descr = value

    @property
    def experiences(self):
        return self.__experiences

    def addExperience(self, time: str, descr: str):
        self.experiences.append({"time": time, "descr": descr})

    @property
    def skills(self):
        return self.__skills

    def addSkill(self, descr: str):
        self.skills.append(descr)

    @property
    def training(self):
        return self.__training

    @training.setter
    def training(self, value: str):
        self.__training = value
