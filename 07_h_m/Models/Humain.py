from Models.Heros import Heros

class Humain(Heros):
    def __init__(self, x: int, y: int):
        super().__init__(11, 1, 1, x, y)  ## bonus: endurance à 1, force à 1
