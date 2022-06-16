from random import randint

class Des:
    def __init__(self, mn: int, mx: int):
        if mx <= mn:
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

    def lance(self) -> int:
        return randint(self.mn, self.mx)

    def bestOf(self, nl: int, nb: int):
        jets = []
        for i in range(0, nl):
            l = self.lance()
            jets.insert(i, -1)
            j = 0
            while (j < i) and (l < jets[j]):
                j += 1
            if j < i:
                for k in range(i, j, -1):
                    jets[k] = jets[k - 1]
            jets[j] = l
        t = 0
        for i in range(0, nb):
            t += jets[i]
        return t
