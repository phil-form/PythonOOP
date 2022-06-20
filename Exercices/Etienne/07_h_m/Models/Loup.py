from Models.Monstre import Monstre
from Models.Des import Des

de4 = Des(1, 4)

class Loup(Monstre):
    def __init__(self, x: int, y: int):
        super().__init__(21, 0, 0, 0, de4.lance(), x, y)  ## pas de bonus d'endurance
                                                          ##              de force
                                                          ## pas d'or
                                                          ## du cuir
