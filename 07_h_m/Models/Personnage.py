from Models.Des import Des

de4 = Des(1, 6)
de6 = Des(1, 6)

class Personnage:
    def __init__(self, pers: int, bEnr: int, bFor: int, gold: int, cuir: int):
        self.pers   = pers ## 11: humain, 12: nain, 21: loup, 22: orque, 23: dragonnet
        self.__end  = de6.bestOf(4, 3) + bEnr
        self.__for  = de6.bestOf(4, 3) + bFor
        self.__pv   = self.pvSet()
        self.__curV = self.__pv
        self.gold   = gold
        self.cuir   = cuir

    @property
    def pers(self):
        return self.__pers
    
    @pers.setter
    def pers(self, v: int):
        if (v != 11) and (v != 12) and (v != 21) and (v != 22) and (v != 23):
            raise ValueError()
        self.__pers = v

    @property
    def endur(self):
        return self.__end

    @property
    def force(self):
        return self.__for

    @property
    def pv(self):
        return self.__pv

    def pvSet(self) -> int:
        return self.__mod(self.endur)

    @property
    def curV(self):
        return self.__curV

    @curV.setter
    def curV(self, v):
        self.__curV = v

    def frappe(self, adv):
        d = de4.lance() + self.__mod(self.force)
        adv.curV -= d
        print(f"{self.nom()} frappe {adv.nom()} avec une force de {d}: il reste {adv.curV} à {adv.nom()}")
        if adv.curV <= 0:
            adv.curV = 0
            if self.pers < 20:
                self.gold += adv.gold
                self.cuir += adv.cuir
    
    def __mod(self, car: int) -> int:
        if car < 5:
            m = -1
        elif car < 10:
            m = 0
        elif car < 15:
            m = 1
        else:
            m = 2
        return (car + m)

    def nom(self) -> str:
        if self.pers == 11:
            s = "Humain"
        elif self.pers == 12:
            s = "Nain"
        elif self.pers == 21:
            s = "Loup"
        elif self.pers == 22:
            s = "Orque"
        elif self.pers == 23:
            s = "Dragonnet"
        else:
            s = "???"
        return s
    
    def __str__(self) -> str:
        return f"{self.nom()}: PV: {self.curV}, force: {self.force}, endurance: {self.endur}, or: {self.gold}, cuir; {self.cuir}"
