from random import randint

class Creature:
    def __init__(self, nom, pdv, force, vitesse, armure) -> None:
        if(pdv + force + vitesse + armure) > 42:
            raise ValueError()
        
        self.__nom = nom
        self.pdv = pdv
        self.__pdvActuel = pdv
        self.force = force
        self.vitesse = vitesse
        self.armure = armure
        self.__armurMax = armure
        self.__modeEsquive = False
        self.__modeProtection = False

    # region properties
    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value: str):
        self.__nom = value

    @property
    def pdv(self):
        return self.__pdv

    @pdv.setter
    def pdv(self, value: int):
        if value > 30 or value < 15:
            raise ValueError()
        self.__pdv = value

    @property
    def force(self):
        return self.__force

    @force.setter
    def force(self, value: int):
        if value > 11 or value < 1:
            raise ValueError()
        self.__force = value

    @property
    def vitesse(self):
        return self.__vitesse
        
    @vitesse.setter
    def vitesse(self, value: int):
        if value > 10 or value < 1:
            raise ValueError()
        self.__vitesse = value

    @property
    def armure(self):
        return self.__armure
        
    @armure.setter
    def armure(self, value: int):
        if value > 10 or value < 0:
            raise ValueError()
        self.__armure = value

    @property
    def tauxEsquive(self):
        esquive = 20 * (self.vitesse / 10)

        if self.__modeEsquive:
            esquive += 50
        
        return esquive

    @property
    def estKo(self):
        return self.__pdvActuel <= 0

    # endregion

    # region methodes

    def preparerEsquive(self):
        self.__modeEsquive = True

    def seProtoger(self):
        self.__armure = self.__armurMax

        self.__modeProtection = True

    def terminerTour(self):
        self.__modeEsquive = False
        self.__modeProtection = False

    def attaquer(self, cible):
        degats = self.force

        if randint(1, 100) <= 5:
            degats *= 2

        cible.subirAttaque(degats)

    def subirAttaque(self, degats):
        if randint(1, 100) > self.tauxEsquive:
            self.subirDegats(degats)

    def subirDegats(self, degats):
        if self.__modeProtection:
            degats /= 2

        if self.__armure >= degats:
            self.__armure -= degats
        else:
            self.__pdvActuel -= degats - self.armure
            self.armure = 0

    def __str__(self) -> str:
        return f"{self.nom} pv : {self.__pdvActuel}/{self.pdv} ar : {self.__armure}/{self.__armurMax}"

        