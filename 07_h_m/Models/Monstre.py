from Models.Personnage import Personnage

from Models.Des        import Des

de10 = Des(0, 9)

class Monstre(Personnage):
    def __init__(self, pers: int, bEnd: int, bFor: int, gold: int, cuir: int):
        if (pers != 21) and (pers != 22) and (pers != 23):
            raise ValueError()
        super().__init__(pers, bEnd, bFor, gold, cuir)

    def alives(lst) -> int:
        mm = list(lst)
        n = 0
        for m in mm:
            n += m.curV
        return n

    def next(lst) -> int:
        mm = list(lst)
        if Monstre.alives(mm) == 0:
            return -1

        m = de10.lance()
        while mm[m].curV == 0:
            m = de10.lance()
        return m
