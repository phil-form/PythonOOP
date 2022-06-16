from Models.Monstre import Monstre
from Models.Des import Des

de4 = Des(1, 4)
de6 = Des(1, 6)

class Dragonnet(Monstre):
    def __init__(self):
        super().__init__(23, 1, 0, de6.lance(), de4.lance())
