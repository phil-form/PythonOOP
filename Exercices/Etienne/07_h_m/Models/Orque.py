from Models.Monstre import Monstre
from Models.Des import Des

de6 = Des(1, 6)

class Orque(Monstre):
    def __init__(self, x: int, y: int):
        super().__init__(22, 0, 1, de6.lance(), 0, x, y)  ## pas de bonus d'endurance
                                                          ## bonus de force à 1
                                                          ## de l'or
                                                          ## pas de cuir
