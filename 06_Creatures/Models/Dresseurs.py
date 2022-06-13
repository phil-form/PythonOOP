from Models.Creatures import Creature

class Dresseur:
    def __init__(self, nom) -> None:
        self.__nom = nom
        self.__maxCreatures = 3
        self.__creatures = []
        self.__activeCreature = None

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value: str):
        self.__nom = value

    @property
    def creatures(self):
        return tuple(self.__creatures)

    @property
    def activeCreature(self) -> Creature:
        return self.__activeCreature

    @property
    def nbCreature(self):
        return len(self.__creatures)

    @property
    def estVaincu(self):
        vaincu = True
        
        for crea in self.creatures:
            if not crea.estKo:
                vaincu = False

        return vaincu

    def ajouterCreature(self, creature: Creature):
        if len(self.__creatures) < self.__maxCreatures:
            self.__creatures.append(creature)

    def  debutMatch(self):
        if self.estVaincu:
            raise ValueError()

        for crea in self.creatures:
            if not crea.estKo:
                self.__activeCreature = crea

    def terminerMatch(self):
        self.__activeCreature = None

    def ordreAttaquer(self, creature):
        self.activeCreature.attaquer(creature)

    def ordreEsquive(self):
        self.activeCreature.preparerEsquive()

    def ordreDefense(self):
        self.activeCreature.seProtoger()

    def changerCreature(self, position):
        if not self.__creatures[position].estKo:
            self.__activeCreature = self.__creatures[position]
            return True

        return False

    def __str__(self) -> str:
        nbOk = 0

        for creature in self.creatures:
            if not creature.estKo:
                nbOk += 1
        return f"{self.nom} creature ok : {nbOk}/{len(self.creatures)}"