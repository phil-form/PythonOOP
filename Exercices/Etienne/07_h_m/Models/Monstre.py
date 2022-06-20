from Models.Personnage import Personnage

from Models.Des        import Des

class Monstre(Personnage):
    def __init__(self, pers: int, bEnd: int, bFor: int, gold: int, cuir: int, x, y):
        if (pers != 21) and (pers != 22) and (pers != 23):
            raise ValueError()
        super().__init__(pers, bEnd, bFor, gold, cuir, x, y)

    ## calcule le total des points de vie de tous les monstres
    ## prend en paramètre un tableau de monstres
    def alives(lst) -> int:
        mm = list(lst)
        n = 0
        for m in mm:
            n += m.curV
        return n

    ## sélectionne de manière aléatoire un monstre qui n'est pas encore mort
    ## prend en paramètre un tableau de monstres
    ## renvoie l'index dans le tableau des monstres
    ##         -1 si tous les monstres sont morts
    def next(lst) -> int:
        mm = list(lst)
        dem = Des(0, len(mm) - 1)
        if Monstre.alives(mm) == 0:
            return -1

        m = dem.lance()
        while mm[m].curV == 0:
            m = dem.lance()
        return m
