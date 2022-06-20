from Models.Monstre import Monstre
from Models.Des import Des

de4 = Des(1, 4)
de6 = Des(1, 6)

class Dragonnet(Monstre):
    def __init__(self, x: int, y: int):
        super().__init__(23, 1, 0, de6.lance(), de4.lance(), x, y)  ## bonus d'endurance à 1
                                                                    ## pas de bonus de force
                                                                    ## de l'or
                                                                    ## du cuir
