from Models.Personnage import Personnage

class Heros(Personnage):
    def __init__(self, pers: int, bEnd: int, bFor: int):
        if (pers != 11) and (pers != 12):
            raise ValueError()
        super().__init__(pers, bEnd, bFor, 0, 0)
