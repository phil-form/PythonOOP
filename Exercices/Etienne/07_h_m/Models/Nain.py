from Models.Heros import Heros

class Nain(Heros):
    def __init__(self, x: int, y: int):
        super().__init__(12, 0, 2, x, y)  ## bonus: endurance à 0, force à 2
