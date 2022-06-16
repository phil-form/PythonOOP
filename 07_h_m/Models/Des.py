from random import randint

class Des:
    def __init__(self, mn: int, mx: int):
        if mx <= mn:            ## il faut que la borne inférieure soit strictement plus petite que la borne supérieure
            raise ValueError()
        self.mn = mn
        self.mx = mx

    @property
    def mn(self):
        return self.__mn

    @mn.setter
    def mn(self, v: int):
        self.__mn = v

    @property
    def mx(self):
        return self.__mx

    @mx.setter
    def mx(self, v: int):
        self.__mx = v

    ## lance 1 x 1 dé
    def lance(self) -> int:
        return randint(self.mn, self.mx)

    ## lance nl (Nombre de Lancers) x le dé, renvoie la somme des nb (Nombre de Bests) meilleurs lancers
    def bestOf(self, nl: int, nb: int):
        jets = []                               ## crée un tableau vide
        for i in range(0, nl):                  ## nombre de lancers
            l = self.lance()                    ## lance ...
            jets.insert(i, -1)                  ## ajoute n'importe quoi à la fin
            j = 0                       
            while (j < i) and (l < jets[j]):    ## cherche où insérer (trie du plus grand au plus petit)
                j += 1
            if j < i:                           ## doit insérer
                for k in range(i, j, -1):       ## donc doit décaler
                    jets[k] = jets[k - 1]
            jets[j] = l                         ## insère à la bonne place

        t = 0                                   ## calcule la somme des nb premiers
        for i in range(0, nb):
            t += jets[i]

        return t
